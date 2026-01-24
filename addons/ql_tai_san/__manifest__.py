{
    'name': 'Quản lý Tài sản',
    'depends': ['base', 'nhan_su', 'ql_tai_chinh'], 
    'data': [
        'security/ir.model.access.csv',
        'views/tai_san_view.xml',
        'views/nhan_vien_inherit_view.xml',
    ],
}