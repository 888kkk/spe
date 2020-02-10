import abc
import json
import secrets


class AbsHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def register(self, username, password):
        pass
    @abc.abstractmethod
    def signin(self, username, password):
        pass
    @abc.abstractmethod
    def add_incedent(self, username, incedent):
        pass
    @abc.abstractmethod
    def update_incident(self, username, incedent_id, incedent):
        pass
    @abc.abstractmethod
    def update_incident_status(self, username, incedent_id, status):
        pass
    def handleRequest(self, req):
        if (req.get("jsonrpc") != "2.0"):
            raise NotImplementedError()
        id = req.get("id")
        method = req.get("method")
        params = req.get("params")
        try:
            o = getattr(self, method)(**params)
            return {
                "jsonrpc": "2.0",
                "id": id,
                "result": json.dumps(o, default=lambda _o: _o.__dict__)
            }
        except:
            raise Exception()


class Handler(AbsHandler):
    def __init__(self, db):
        self.db = db
    def register(self, username, firstname, lastname, password):
        self.db[username] = {
            "username": username,
            "firstname": firstname,
            "lastname": lastname,
            "password": password,
            "incidents": {}
        }
        return {
            "username": username,
            "firstname": firstname,
            "lastname": lastname,
            "incidents": {}
        }
    def signin(self, username, password):
        if (self.db.get(username, {}).get("password") == password):
            user = self.db[username]
            return {
                "username": user["username"],
                "firstname": user["firstname"],
                "lastname": user["lastname"],
                "incidents": user["incidents"]
            }
        raise Exception("invalid credentials")
    def add_incedent(self, username, incedent):
        id = secrets.token_hex(32)
        user = self.db[username]
        user["incidents"][id]["data"] = incedent
        user["incidents"][id]["status"] = "created"
        return user["incidents"][id]
    def update_incident(self, username, incedent_id, incedent):
        id = secrets.token_hex(32)
        user = self.db[username]
        user["incidents"][id]["data"] = incedent
        user["incidents"][id]["status"] = "created"
        return user["incidents"][id]
    def update_incident_status(self, username, incedent_id, status):
        user = self.db[username]
        user["incidents"][incedent_id]["status"] = status
        return user["incidents"][incedent_id]


if __name__ == "__main__":
    db = {}
    handler = Handler(db)
    handler.register("barinas", "sebastian", "barinas", "barinas")
    print(1, db)
    handler.signin("barinas", "barinas")
    print(db)