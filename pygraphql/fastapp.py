from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from schema import schema

app = FastAPI()

app.add_route("/graphiql", GraphQLApp(schema=schema))
