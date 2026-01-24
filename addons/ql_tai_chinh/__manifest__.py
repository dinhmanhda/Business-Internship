{
    'name': 'Quản lý Tài chính',
    'version': '1.0',
    'depends': ['base', 'nhan_su',], # Thêm 'ql_tai_san' vào đây
    'data': [
        'security/ir.model.access.csv',
        'views/tai_chinh_view.xml',
        'views/nhan_vien_inherit_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}