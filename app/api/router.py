import falcon
from handler.Persons import PersonHandler
from handler.PersonDetail import PersonDetailHandler
from handler.PersonSearch import PersonSearchHandler

routes = {
    "/person": PersonHandler(),
    "/person/{phone:int}": PersonDetailHandler(),
    "/person/search/{mode}/{value}": PersonSearchHandler()
}