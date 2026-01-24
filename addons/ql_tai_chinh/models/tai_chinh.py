from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta

class QuanLyTaiChinh(models.Model):
    _name = 'quan.ly.tai.chinh'
    _description = 'Quản lý Tài chính và Khấu hao'

    name = fields.Char(string='Số phiếu', required=True, default='New')
    noi_dung = fields.Char(string='Nội dung')
    so_tien = fields.Float(string='Số tiền/Nguyên giá', required=True)
    ngay_lap = fields.Date(string='Ngày lập', default=fields.Date.today)
    thoi_gian_khau_hao = fields.Integer(string='Thời gian khấu hao (tháng)', default=12)
    loai_phieu = fields.Selection([('thu', 'Thu'), ('chi', 'Chi')], string='Loại phiếu', default='chi')
    trang_thai = fields.Selection([('nhap', 'Dự thảo'), ('xac_nhan', 'Đã xác nhận')], string='Trạng thái', default='nhap')
    
    nhan_vien_id = fields.Many2one('nhan_vien', string='Nhân viên')
    
    # Giữ nguyên để liên kết, nhưng trong __manifest__.py của QLTC phải XÓA 'ql_tai_san' khỏi 'depends'
    tai_san_id = fields.Many2one('quan.ly.tai.san', string='Tài sản gốc')

    khau_hao_thang = fields.Float(string='Khấu hao/tháng', compute='_compute_depreciation', store=True)
    khau_hao_luy_ke = fields.Float(string='Khấu hao lũy kế', compute='_compute_depreciation', store=True)
    gia_tri_con_lai = fields.Float(string='Giá trị còn lại', compute='_compute_depreciation', store=True)

    @api.depends('so_tien', 'thoi_gian_khau_hao', 'ngay_lap')
    def _compute_depreciation(self):
        for rec in self:
            # Logic tính toán dựa trên thời gian thực tế (Hôm nay là 2026-01-24)
            if rec.so_tien and rec.thoi_gian_khau_hao > 0 and rec.ngay_lap:
                rec.khau_hao_thang = rec.so_tien / rec.thoi_gian_khau_hao
                
                d1 = rec.ngay_lap
                d2 = date.today()
                
                # Tính số tháng chênh lệch
                diff = relativedelta(d2, d1)
                month_diff = diff.years * 12 + diff.months
                
                # Giới hạn số tháng khấu hao không vượt quá vòng đời
                months = max(0, min(month_diff, rec.thoi_gian_khau_hao))
                
                rec.khau_hao_luy_ke = rec.khau_hao_thang * months
                rec.gia_tri_con_lai = rec.so_tien - rec.khau_hao_luy_ke
            else:
                rec.khau_hao_thang = 0
                rec.khau_hao_luy_ke = 0
                rec.gia_tri_con_lai = rec.so_tien

class NhanVienInheritTC(models.Model):
    _inherit = 'nhan_vien'

    tai_chinh_ids = fields.One2many('quan.ly.tai.chinh', 'nhan_vien_id', string='Lịch sử Tài chính')