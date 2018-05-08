# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Odoo - Universitas",
    "version": "8.0.1.0.0",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "hr",
    ],
    "data": [
        "security/res_groups_data.xml",
        "wizards/cancel_reason_views.xml",
        "views/aktivitas_mk_views.xml",
        "views/registrasi_views.xml",
        "views/semester_views.xml",
        "views/fakultas_views.xml",
        "views/program_studi_views.xml",
        "views/mata_kuliah_views.xml",
        "views/jadwal_views.xml",
        "views/kelas_views.xml",
        "views/absen_views.xml",
        "views/mahasiswa_views.xml",
        "views/dosen_views.xml",
        "views/dosen_baru_views.xml",
        "views/menu.xml"
    ],
}
