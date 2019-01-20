from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api, Resource
from controllers.RoleController import GetRole, InsertRole, UpdateRole, DeleteRole
import utility
import os

load_dotenv()

app = Flask(__name__)
api = Api(app)
app.config['JSON_SORT_KEYS'] = False


class GetVersion(Resource):
    @staticmethod
    def get():
        return utility.give_response("00", os.getenv('APP_NAME'))


@app.errorhandler(404)
def page_not_found(e):
    return utility.give_response("01", str(e))


api.add_resource(GetVersion, '/')
api.add_resource(GetRole, '/getRole')
api.add_resource(InsertRole, '/insertRole')
api.add_resource(UpdateRole, '/updateRole/<string:sysrole_kode>')
api.add_resource(DeleteRole, '/deleteRole/<string:sysrole_kode>')

if __name__ == '__main__':
    app.run()
