
DB="test.db"

function table_exists(){
Q="SELECT name FROM sqlite_master WHERE type='table' AND name='$1';"
R=`sqlite3 $DB "$Q"`
if [ "$R" = "$1" ]; then
echo 1
else
echo 0
fi
}


function addFunction {
STATE=$( table_exists "postData" )
if [ "$STATE" -eq 0 ]; then
sqlite3 $DB "CREATE TABLE postData (id INTEGER PRIMARY KEY, title TEXT, content TEXT);"
else
echo "TABLE ALREADY EXISTS"
fi
title=$1
content=$2
data=`sqlite3 test.db "SELECT id FROM postData ORDER BY id DESC LIMIT 1;";`
if [ "$data" == "" ]; then
  query="INSERT INTO postData VALUES (1,'$title','$content');"
else
  id=$(( $data+1 ))
  query="INSERT INTO postData VALUES ($id,'$title','$content');"
fi
sqlite3 $DB "$query"
}

function showPost {
STATE=$( table_exists "postData" )
if [ "$STATE" -eq 1 ]; then
  sqlite3 $DB "select * from postData"
else
echo "TABLE NOT EXISTS"
fi
}

function searchPost {
searchKeyword=$1
Data=`sqlite3 $DB "select * from postData"`
for i in $Data
do
  if [[ "$i" = *"$1"* ]]
  then
    echo "$i"
  fi
  
done

}

help () {
    cat <<EOF
blog.sh --help will list help 
blog.sh post add "title" "content" will add a new blog a new blog post with title and content.
blog.sh post list will list all blog posts
blog.sh post search "keyword" will list all blog posts where “keyword” is found in title and/or content.
blog.sh category add "category-name" create a new category
blog.sh category list list all categories
blog.sh category assign <post-id> <cat-id> assign category to post
blog.sh post add "title" "content" --category "cat-name" will add a new blog a new blog post 
EOF
}


argument1=$1
if [ "$argument1" == "--help" ]; then
  help
elif [ "$argument1" == "post" ]
  then
  if [[ "x$2" = "xadd" ]]; then
    addFunction $3 $4

  elif [[ "x$2" = "xlist" ]];
  then
    showPost
  elif [[ "x$2" = "xsearch" ]];
  then
    searchPost $3
  fi
fi
