import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QCheckBox, QPushButton, QFileDialog
)
from PyQt5.QtGui import QFontDatabase, QFont, QIcon
from PyQt5.QtCore import Qt

class ProjectExportTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("项目文件导出工具")
        self.setGeometry(100, 100, 500, 400)  # 调整窗口大小
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # 加载图标
        icon_path = os.path.join(os.path.dirname(__file__), 'icon-3种尺寸.ico')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print("图标文件未找到")

        # 加载并设置字体
        font_path = os.path.join(os.path.dirname(__file__), 'HarmonyOS_Sans_SC_Regular.ttf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            font = QFont(font_family, 12)  # 增加基础字体大小
            self.setFont(font)
        else:
            print("字体加载失败，使用系统默认字体")

        # 创建标题
        title_label = QLabel("项目文件导出工具", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; margin: 15px 0;")
        self.layout.addWidget(title_label)

        # 创建拖拽框
        self.drag_label = QLabel("拖入项目文件夹", self)
        self.drag_label.setAlignment(Qt.AlignCenter)
        self.drag_label.setStyleSheet("""
            QLabel {
                border: 2px dashed #aaa;
                border-radius: 5px;
                padding: 30px;
                background-color: #f8f8f8;
                color: #555;
                font-size: 16px;
            }
        """)
        self.drag_label.setMinimumHeight(120)
        self.layout.addWidget(self.drag_label)

        # 创建选择文件夹按钮
        self.select_button = QPushButton("选择文件夹", self)
        self.select_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 4px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.select_button.clicked.connect(self.select_folder)
        self.layout.addWidget(self.select_button)

        # 创建复选框
        self.export_tree_only_checkbox = QCheckBox("只导出文件结构", self)
        self.export_tree_only_checkbox.setStyleSheet("font-size: 14px; margin-top: 10px;")
        self.layout.addWidget(self.export_tree_only_checkbox)

        # 创建状态编辑框
        self.status_edit = QLineEdit(self)
        self.status_edit.setReadOnly(True)
        self.status_edit.setPlaceholderText('输出状态将显示在这里')
        self.status_edit.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 4px;
                background-color: #f9f9f9;
                font-size: 14px;
            }
        """)
        self.layout.addWidget(self.status_edit)

        self.central_widget.setLayout(self.layout)
        self.setAcceptDrops(True)

    def select_folder(self):
        dir_path = QFileDialog.getExistingDirectory(self, "选择项目文件夹")
        if dir_path:
            self.process_folder(dir_path)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            dir_path = urls[0].toLocalFile()
            self.process_folder(dir_path)

    def process_folder(self, dir_path):
        if os.path.isdir(dir_path):
            self.status_edit.clear()
            project_name = os.path.basename(dir_path)
            if self.export_tree_only_checkbox.isChecked():
                output_file = os.path.join(dir_path, f'{project_name}_文件结构.txt')
            else:
                output_file = os.path.join(dir_path, f'{project_name}_文结构和内容.txt')
            self.generate_file_structure(dir_path, output_file)
            self.status_edit.setText(f'导出完成：{output_file}')

    def generate_file_structure(self, root_dir, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(self.get_directory_tree(root_dir, output_file))
            if not self.export_tree_only_checkbox.isChecked():
                for dirpath, _, filenames in os.walk(root_dir):
                    for filename in filenames:
                        filepath = os.path.join(dirpath, filename)
                        if filepath == output_file:
                            continue
                        normalized_path = os.path.normpath(filepath).replace('\\', '/')
                        f.write(f"\n<file path=\"{normalized_path}\">\n")
                        try:
                            with open(filepath, 'r', encoding='utf-8') as file:
                                content = file.read()
                                f.write(content + "\n")
                        except Exception as e:
                            f.write(f"无法读取文件内容: {e}\n")
                        f.write("</file>\n")

    def get_directory_tree(self, root_dir, output_file):
        tree = []
        for dirpath, dirnames, filenames in os.walk(root_dir):
            level = dirpath.replace(root_dir, '').count(os.sep)
            indent = '│   ' * (level)
            tree.append(f"{indent}├── {os.path.basename(dirpath)}/")
            subindent = '│   ' * (level + 1)
            for f in filenames:
                if os.path.join(dirpath, f) == output_file:
                    continue
                tree.append(f"{subindent}├── {f}")
        return "\n".join(tree) + "\n"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # 设置全局字体
    font_path = os.path.join(os.path.dirname(__file__), 'HarmonyOS_Sans_SC_Regular.ttf')
    font_id = QFontDatabase.addApplicationFont(font_path)
    if font_id != -1:
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family, 12)  # 增加基础字体大小
        app.setFont(font)

    mainWin = ProjectExportTool()
    mainWin.show()
    sys.exit(app.exec_())