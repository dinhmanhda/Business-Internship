from odoo import models, fields, api

class QuanLyTaiSan(models.Model):
    _name = 'quan.ly.tai.san'
    _description = 'Quản lý Tài sản'

    name = fields.Char(string='Tên tài sản', required=True)
    ma_tai_san = fields.Char(string='Mã tài sản')
    ngay_mua = fields.Date(string='Ngày mua', default=fields.Date.today)
    gia_tri_goc = fields.Float(string='Nguyên giá', required=True)
    thoi_gian_khau_hao = fields.Integer(string='Vòng đời (tháng)', default=12)
    nguoi_phu_trach_id = fields.Many2one('nhan_vien', string='Người phụ trách')
    
    phieu_ke_toan_id = fields.Many2one('quan.ly.tai.chinh', string='Bản ghi kế toán', readonly=True)
    
    khau_hao_thang = fields.Float(
        related='phieu_ke_toan_id.khau_hao_thang', 
        string='Khấu hao/tháng', 
        store=True
    )
    gia_tri_con_lai = fields.Float(
        related='phieu_ke_toan_id.gia_tri_con_lai', 
        string='Giá trị còn lại', 
        store=True
    )

    trang_thai = fields.Selection([
        ('moi', 'Mới'), 
        ('dang_su_dung', 'Đang sử dụng')
    ], string='Trạng thái', default='moi')

    # THÊM TRƯỜNG GHI CHÚ TẠI ĐÂY
    ghi_chu = fields.Text(string='Ghi chú hiện trạng')

    def action_confirm_and_link_finance(self):
        for rec in self:
            if not rec.phieu_ke_toan_id:
                nv_id = rec.nguoi_phu_trach_id.id if rec.nguoi_phu_trach_id else False
                phieu = self.env['quan.ly.tai.chinh'].create({
                    'name': f'CHI/{rec.ma_tai_san or "TS"}',
                    'so_tien': rec.gia_tri_goc,
                    'ngay_lap': rec.ngay_mua,
                    'thoi_gian_khau_hao': rec.thoi_gian_khau_hao,
                    'tai_san_id': rec.id,
                    'nhan_vien_id': nv_id,
                    'trang_thai': 'xac_nhan',
                })
                rec.write({'phieu_ke_toan_id': phieu.id, 'trang_thai': 'dang_su_dung'})
        return True

class NhanVienInheritTS(models.Model):
    _inherit = 'nhan_vien'
    tai_san_ids = fields.One2many('quan.ly.tai.san', 'nguoi_phu_trach_id', string='Tài sản phụ trách')