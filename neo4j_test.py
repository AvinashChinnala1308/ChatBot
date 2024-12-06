from neo4j import GraphDatabase

uri = "bolt://localhost:7687"  # Default URI for local Neo4j
username = "neo4j"             # Default username
password = "neo4jPassword"     # Replace with your database password

driver = GraphDatabase.driver(uri, auth=(username, password))

try:
    with driver.session() as session:
        session.run("CREATE (TestNode:Example {name: 'HelloNeo4j'})")
        print("Data added to Neo4j!")
finally:
    driver.close()
