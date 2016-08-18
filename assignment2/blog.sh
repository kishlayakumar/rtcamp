
DB="test.db"

function table_exists(){
Q="SELECT name FROM sqlite_master WHERE type=’table’ AND name='$1';"
R=`sqlite3 $DB "$Q"`
if [ "$R" = "$1" ]; then
echo 1
else
echo 0
fi
}


function addFunction {
STATE=$( table_exists "postData" )
if [ "$STATE" -gt 0 ]; then
sqlite3 $DB “CREATE TABLE postData (id INTEGER PRIMARY KEY, title TEXT, content TEXT);”
else
echo “TABLE ALREADY EXISTS”
fi
title=$1
content=$2
data=`sqlite3 test.db "select id from n";`




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
if [[ "$argument1"=="--help" ]]; then
  help
fi
if [[ "$argument1"=="post"]]; then
  if [ "$2"=="add" ];
    addFunction $3 $4
  fi
  
fi
