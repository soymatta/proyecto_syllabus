from database.db import search

id_param_name = 'version_id'

def main(event):
    
    # Header
    try:
        params = event['params']
        
        # Obtiene el version_id.
        params['id'] = params.pop(id_param_name)

    except KeyError as e:
        return f"* Debe enviar el id de la versión. {e}"
    
    # Body
    result = {'status': False, 'data': {}}

    item = search('versions', params)

    result['status'] = bool(item)
    result['data'] = item

    if not result['status']:
        return {
            'status_code': 404,
            'error_message': 'Ingrese un id existente.'
        }

    # Response
    return {'status': bool(result), 'data': result['data']}
    

