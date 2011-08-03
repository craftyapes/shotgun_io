"""defines the default entity types, filters, fields, and order for the list
methods for querying Shotgun for populating menus for artist submissions
""" 
entity_queries = {
    'users': {
        'entity_type': 'HumanUser',
        'filters': [['sg_status_list', 'is_not', 'dis']],
        'fields': ['id','login'],
        'order': [{'field_name':'login','direction':'asc'}],
        'project_required': False,
        'user_required': False,
       },
    'projects': {
        'entity_type': 'Project',
        'filters': [
            ['sg_status', 'is_not', 'Archive'],
            ['name', 'is_not', 'Template Project']],
        'fields': ['id','name'],
        'order': [{'field_name':'name','direction':'asc'}],
        'project_required': False,
        'user_required': False,
        },
    'assets': {
        'entity_type': 'Asset',
        'filters': [['sg_status_list', 'is_not', 'omt']],
        'fields': ['id','code'],
        'order': [{'field_name':'code','direction':'asc'}],
        'project_required': True,
        'user_required': False,
        },
    'shots': {
        'entity_type': 'Shot',
        'filters': [['sg_status_list', 'is_not', 'omt']],
        'fields': ['id','code'],
        'order': [{'field_name':'code','direction':'asc'}],
        'project_required': True,
        'user_required': False,
       },
    'tasks': {
        'entity_type': 'Task',
        'filters': [['sg_status_list','is','ip']],
        'fields': ['id','content','entity','project'],
        'order': [
            {'field_name':'project','direction':'asc'},
            {'field_name':'entity','direction':'asc'},
            {'field_name':'content','direction':'asc'}],
        'project_required': False,
        'user_required': True,
        },
    'assetsandshots': {
        'project_required': True,
        'user_required': False,
    },
}

"""Defines the default query filter used by validate_user()
"""
validate_user = {
    'entity_type': 'HumanUser',
    'filters': [['sg_status_list', 'is', 'act']],
    'fields': ['id','login'],
}
