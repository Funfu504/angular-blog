#query template for deleting the rows identified by the Migration Runner.

#selector
aws dynamodb query --table-name Blog_Post --key-condition-expression "Post_Id = :id AND Post_Element_Type = :type" --expression-attribute-values '{ \":id\": {\"S\": \"POST#002\"}, \":type\": {\"S\": \"IMAGE\"} }' --endpoint-url http://localhost:8000

#delete
aws dynamodb delete-item --table-name Blog_Post --key '{\"Post_Id\": {\"S\": \"POST#002\"}, \"Post_Element_Type\": {\"S\": \"IMAGE\"}}' --endpoint-url http://localhost:8000