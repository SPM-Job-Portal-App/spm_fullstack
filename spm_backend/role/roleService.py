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
        
    def get_all_role_names():
        try:
            # Query all roles and retrieve only the role names
            roles = Role.query.with_entities(Role.role_name).all()

            # Extract role names from the query result
            role_names = [role[0] for role in roles]

            return role_names
        except Exception as e:
            raise Exception("An error occurred while retrieving role names")

