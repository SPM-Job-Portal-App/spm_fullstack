from models.role_model import Role

class RoleService():
    def get_role_by_role_name(role_name_input):

        try:
            role_response = Role.query.filter(Role.role_name == role_name_input).first()

            role =  {
                'role_name': role_response.role_name,
                'role_desc': role_response.role_desc
            }
            return role
        except Exception as e:
            raise Exception("No role with this role name found")

