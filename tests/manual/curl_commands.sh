#!/bin/bash



echo "ACTION 1 - DB CLEANUP"

PYTHONPATH=. python tests/clear_db.py
table=$(curl -X GET -H "Content-Type: application/json" --silent 'http://127.0.0.1:8000/categories/' | jq .)

if [ "$table" == "[]" ] || [ -z "$table" ]; then
    echo "Database was cleared correctly."
else
    echo "Database was not cleared correctly."
fi

sleep 1


echo "ACTION 2 - DB POPULATION, CHECKING 'GET /categories/'"

PYTHONPATH=. python tests/populate_db.py
table=$(curl -X GET -H "Content-Type: application/json" --silent 'http://127.0.0.1:8000/categories/')
table_size=$(echo "$table" | jq '. | length')


if [[ $table_size == 7 ]]; then
    echo "Database was populated correctly and has 7 elements."
else
    echo "Database was not populated correctly. It doesnt have 7 elements."
fi



echo "ACTION 3 - CHECKING 'GET /categories/<id>'"

category_id=$(curl -X GET -H "Content-Type: application/json" --silent 'http://127.0.0.1:8000/categories/' | jq .[-1].id)

echo
echo "Below you should see GET /categories/$category_id/ response body:"
curl -X GET -H "Content-Type: application/json" --silent "http://127.0.0.1:8000/categories/$category_id/" | jq .
echo


echo "ACTION 4 - CHECKING CREATING NEW CATEGORY 'POST /categories/'"


echo
echo "Now, we are adding new category named 'NewCategory':"
category_id=$(curl -X POST -H "Content-Type: application/json" -d '{"name": "NewCategory"}' --silent  'http://127.0.0.1:8000/categories/' | jq .id)
echo "Below you should see GET /categories/$category_id/ response body:"
curl -X GET -H "Content-Type: application/json" --silent "http://127.0.0.1:8000/categories/$category_id/" | jq .


echo "ACTION 5 - CHECKING UPDATING (FULLY) CATEGORY OBJECT 'PUT /categories/<id>'"

echo "Now, we are changing fully category object named 'NewCategory' to 'NewCategory0' using PUT /categories/$category_id/"
echo "New object looks like:"
curl -X PUT -H "Content-Type: application/json" -d "{\"id\": $category_id, \"name\": \"NewCategory0\", \"parent\": null}"  --silent "http://127.0.0.1:8000/categories/$category_id/" | jq .


echo "ACTION 6 - CHECKING UPDATING (PARTIALLY) CATEGORY OBJECT 'PATCH /categories/<id>'"
echo "Now, we are partially category object named 'NewCategory' to 'NewCategory0' using PATCH /categories/$category_id/"
echo "New object looks like:"
curl -X PATCH -H "Content-Type: application/json" -d '{"name": "NewCategoryX"}' --silent "http://127.0.0.1:8000/categories/$category_id/" | jq .



table=$(curl -X GET -H "Content-Type: application/json" --silent 'http://127.0.0.1:8000/categories/')
table_size=$(echo "$table" | jq '. | length')

echo ""

if [ $table_size == 8 ]; then
    echo "Current database state is correct. Db has 8 elements."
else
    echo "Current database state is not correct. Db doesnt have 8 elements."
fi

echo "Below current category table state (GET /categories/):"
curl -X GET -H "Content-Type: application/json" --silent 'http://127.0.0.1:8000/categories/' | jq .
echo


echo ""
echo "ACTION 7 - CHECKING DELETING CATEGORY OBJECT 'DELETE /categories/<id>'"

category_id=$(curl -X GET -H "Content-Type: application/json" --silent 'http://127.0.0.1:8000/categories/' | jq .[-1].id)
echo "Now, we are removing category object using 'DELETE /categories/$category_id/':"
curl -X DELETE -H "Content-Type: application/json" --silent "http://127.0.0.1:8000/categories/$category_id/" | jq .

table=$(curl -X GET -H "Content-Type: application/json" --silent 'http://127.0.0.1:8000/categories/')
table_size=$(echo "$table" | jq '. | length')


if [ $table_size == 7 ]; then
    echo "Current database state is correct. Db has 7 elements."
else
    echo "Current database state is not correct. Db doesnt have 7 elements."
fi
