from PySide2.QtGui import QColor


COLOR_SCHEMES = {
    'Light': {
        'disasm_view_operand_color': QColor(0x00, 0x00, 0x80),
        'disasm_view_operand_constant_color': QColor(0x00, 0x00, 0x80),
        'disasm_view_variable_label_color': QColor(0x00, 0x80, 0x00),
        'disasm_view_operand_highlight_color': QColor(0xfc, 0xef, 0x00),
        'disasm_view_operand_select_color': QColor(0xff, 0xff, 0x00),
        'disasm_view_function_color': QColor(0x00, 0x00, 0xff),
        'disasm_view_ir_default_color': QColor(0x80, 0x80, 0x80),
        'disasm_view_label_color': QColor(0x00, 0x00, 0xff),
        'disasm_view_label_highlight_color': QColor(0xf0, 0xf0, 0xbf),
        'disasm_view_target_addr_color': QColor(0x00, 0x00, 0xff),
        'disasm_view_antitarget_addr_color': QColor(0xff, 0x00, 0x00),
        'disasm_view_node_shadow_color': QColor(0x00, 0x00, 0x00, 0x00),
        'disasm_view_node_background_color': QColor(0xfa, 0xfa, 0xfa),
        'disasm_view_node_zoomed_out_background_color': QColor(0xda, 0xda, 0xda),
        'disasm_view_node_border_color': QColor(0xf0, 0xf0, 0xf0),
        'disasm_view_node_instruction_selected_background_color': QColor(0xb8, 0xc3, 0xd6),
        'disasm_view_node_address_color': QColor(0x00, 0x00, 0x00),
        'disasm_view_node_mnemonic_color': QColor(0x00, 0x00, 0x80),
        'disasm_view_selected_node_border_color': QColor(0x6b, 0x71, 0x7c),
        'disasm_view_printable_byte_color': QColor(0x00, 0x80, 0x40),
        'disasm_view_printable_character_color': QColor(0x00, 0x80, 0x40),
        'disasm_view_unprintable_byte_color': QColor(0x80, 0x40, 0x00),
        'disasm_view_unprintable_character_color': QColor(0x80, 0x40, 0x00),
        'disasm_view_unknown_byte_color': QColor(0xf0, 0x00, 0x00),
        'disasm_view_unknown_character_color': QColor(0xf0, 0x00, 0x00),
        'function_table_color': QColor(0x00, 0x00, 0x00),
        'function_table_syscall_color': QColor(0x00, 0x00, 0x80),
        'function_table_plt_color': QColor(0x00, 0x80, 0x00),
        'function_table_simprocedure_color': QColor(0x80, 0x00, 0x00),
        'function_table_alignment_color': QColor(0x80, 0x00, 0x80),
        'function_table_signature_bg_color': QColor(0xaa, 0xff, 0xff),
        'palette_window': QColor(0xef, 0xef, 0xef, 0xff),
        'palette_windowtext': QColor(0x00, 0x00, 0x00, 0xff),
        'palette_base': QColor(0xff, 0xff, 0xff, 0xff),
        'palette_alternatebase': QColor(0xf7, 0xf7, 0xf7, 0xff),
        'palette_tooltipbase': QColor(0xff, 0xff, 0xdc, 0xff),
        'palette_tooltiptext': QColor(0x00, 0x00, 0x00, 0xff),
        'palette_text': QColor(0x00, 0x00, 0x00, 0xff),
        'palette_button': QColor(0xef, 0xef, 0xef, 0xff),
        'palette_buttontext': QColor(0x00, 0x00, 0x00, 0xff),
        'palette_brighttext': QColor(0xff, 0xff, 0xff, 0xff),
        'palette_highlight': QColor(0x30, 0x8c, 0xc6, 0xff),
        'palette_highlightedtext': QColor(0xff, 0xff, 0xff, 0xff),
        'palette_disabled_text': QColor(0xbe, 0xbe, 0xbe, 0xff),
        'palette_disabled_buttontext': QColor(0xbe, 0xbe, 0xbe, 0xff),
        'palette_disabled_windowtext': QColor(0xbe, 0xbe, 0xbe, 0xff),
        'palette_light': QColor(0xff, 0xff, 0xff, 0xff),
        'palette_midlight': QColor(0xca, 0xca, 0xca, 0xff),
        'palette_dark': QColor(0x9f, 0x9f, 0x9f, 0xff),
        'palette_mid': QColor(0xb8, 0xb8, 0xb8, 0xff),
        'palette_shadow': QColor(0x76, 0x76, 0x76, 0xff),
        'palette_link': QColor(0x00, 0x00, 0xff, 0xff),
        'palette_linkvisited': QColor(0xff, 0x00, 0xff, 0xff),
        'feature_map_color_regular_function': QColor(0x00, 0xa0, 0xe8),
        'feature_map_color_unknown': QColor(0x0a, 0x0a, 0x0a),
        'feature_map_color_delimiter': QColor(0x00, 0x00, 0x00),
        'feature_map_color_data': QColor(0xc0, 0xc0, 0xc0),
        'pseudocode_comment_color': QColor(0x00, 0x80, 0x00, 0xff),
        'pseudocode_function_color': QColor(0x00, 0x00, 0xff, 0xff),
        'pseudocode_quotation_color': QColor(0x00, 0x80, 0x00, 0xff),
        'pseudocode_keyword_color': QColor(0x00, 0x00, 0x80, 0xff),
    },

    'Dark': {
        'disasm_view_operand_color': QColor(0xf0, 0xf0, 0x5a),
        'disasm_view_operand_constant_color': QColor(0x34, 0xf0, 0x8c),
        'disasm_view_variable_label_color': QColor(0x34, 0xd4, 0xf0),
        'disasm_view_operand_highlight_color': QColor(0x05, 0x2f, 0x50),
        'disasm_view_operand_select_color': QColor(0x09, 0x50, 0x8d),
        'disasm_view_function_color': QColor(0xc8, 0xc8, 0xc8),
        'disasm_view_ir_default_color': QColor(0x80, 0x80, 0x80),
        'disasm_view_label_color': QColor(0x00, 0xaa, 0xff),
        'disasm_view_label_highlight_color': QColor(0x2f, 0x2f, 0x25),
        'disasm_view_target_addr_color': QColor(0x00, 0x00, 0xff),
        'disasm_view_antitarget_addr_color': QColor(0xff, 0x00, 0x00),
        'disasm_view_node_shadow_color': QColor(0x00, 0x00, 0x00, 0x4b),
        'disasm_view_node_background_color': QColor(0x3c, 0x3c, 0x3c),
        'disasm_view_node_zoomed_out_background_color': QColor(0x64, 0x64, 0x64),
        'disasm_view_node_border_color': QColor(0x50, 0x50, 0x50),
        'disasm_view_node_instruction_selected_background_color': QColor(0x4c, 0x50, 0x58),
        'disasm_view_node_address_color': QColor(0xe0, 0xe0, 0xe0),
        'disasm_view_node_mnemonic_color': QColor(0xe0, 0xe0, 0xe0),
        'disasm_view_selected_node_border_color': QColor(0x6b, 0x71, 0x7c),
        'disasm_view_printable_byte_color': QColor(0x00, 0x80, 0x40),
        'disasm_view_printable_character_color': QColor(0x00, 0x80, 0x40),
        'disasm_view_unprintable_byte_color': QColor(0x80, 0x40, 0x00),
        'disasm_view_unprintable_character_color': QColor(0x80, 0x40, 0x00),
        'disasm_view_unknown_byte_color': QColor(0xf0, 0x00, 0x00),
        'disasm_view_unknown_character_color': QColor(0xf0, 0x00, 0x00),
        'function_table_color': QColor(0xe0, 0xe0, 0xe0),
        'function_table_syscall_color': QColor(0x00, 0x00, 0x80),
        'function_table_plt_color': QColor(0x00, 0x80, 0x00),
        'function_table_simprocedure_color': QColor(0x80, 0x00, 0x00),
        'function_table_alignment_color': QColor(0x80, 0x80, 0x00),
        'function_table_signature_bg_color': QColor(0xaa, 0xff, 0xff),
        'palette_window': QColor(0x35, 0x35, 0x35),
        'palette_windowtext': QColor(0xff, 0xff, 0xff),
        'palette_base': QColor(0x28, 0x28, 0x28),
        'palette_alternatebase': QColor(0x35, 0x35, 0x35),
        'palette_tooltipbase': QColor(0x35, 0x35, 0x35),
        'palette_tooltiptext': QColor(0xff, 0xff, 0xff),
        'palette_text': QColor(0xff, 0xff, 0xff),
        'palette_button': QColor(0x35, 0x35, 0x35),
        'palette_buttontext': QColor(0xff, 0xff, 0xff),
        'palette_brighttext': QColor(0xff, 0x00, 0x00),
        'palette_highlight': QColor(0x28, 0x28, 0x28).lighter(),
        'palette_highlightedtext': QColor(0xff, 0xff, 0xff),
        'palette_disabled_text': QColor(0x80, 0x80, 0x80),
        'palette_disabled_buttontext': QColor(0x80, 0x80, 0x80),
        'palette_disabled_windowtext': QColor(0x80, 0x80, 0x80),
        'palette_light': QColor(0x00, 0x00, 0x00),
        'palette_midlight': QColor(0x00, 0x00, 0x00),
        'palette_dark': QColor(0x00, 0x00, 0x00),
        'palette_mid': QColor(0x46, 0x46, 0x46),
        'palette_shadow': QColor(0x00, 0x00, 0x00),
        'palette_link': QColor(0x2d, 0xc5, 0x2d).lighter(),
        'palette_linkvisited': QColor(0x2d, 0xc5, 0x2d).darker(),
        'feature_map_color_regular_function': QColor(0x00, 0xa0, 0xe8),
        'feature_map_color_unknown': QColor(0x0a, 0x0a, 0x0a),
        'feature_map_color_delimiter': QColor(0x00, 0x00, 0x00),
        'feature_map_color_data': QColor(0xc0, 0xc0, 0xc0),
        'pseudocode_comment_color': QColor(0x00, 0x80, 0x00, 0xff),
        'pseudocode_function_color': QColor(0x60, 0x80, 0xff, 0xff),
        'pseudocode_quotation_color': QColor(0x00, 0x80, 0x00, 0xff),
        'pseudocode_keyword_color': QColor(0x00, 0xff, 0xff, 0xff),
    }
}
