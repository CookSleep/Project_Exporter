import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLabel, QLineEdit
)
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import Qt

class ProjectExportTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("项目文件导出工具")
        self.setGeometry(100, 100, 600, 300)
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # 加载并设置字体
        font_path = os.path.join(os.path.dirname(__file__), 'HarmonyOS_Sans_SC_Regular.ttf')
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print("字体加载失败")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            font = QFont(font_family, 10)
            self.setFont(font)

        # 创建拖拽框
        self.drag_label = QLabel("拖入项目文件夹", self)
        self.drag_label.setAlignment(Qt.AlignCenter)
        self.drag_label.setStyleSheet("QLabel {border: 1px dashed #ccc; border-radius: 10px; min-height: 150px;}")
        self.drag_label.setFont(font)
        self.layout.addWidget(self.drag_label)

        # 创建状态编辑框
        self.status_edit = QLineEdit(self)
        self.status_edit.setReadOnly(True)
        self.status_edit.setPlaceholderText('输出状态将显示在这里')
        self.status_edit.setFont(font)
        self.layout.addWidget(self.status_edit)

        self.central_widget.setLayout(self.layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            dir_path = urls[0].toLocalFile()
            if os.path.isdir(dir_path):
                self.status_edit.clear()
                project_name = os.path.basename(dir_path)
                output_file = os.path.join(dir_path, f'{project_name}_结构和代码.txt')
                self.generate_file_structure(dir_path, output_file)
                self.status_edit.setText(f'导出完成：{output_file}')

    def generate_file_structure(self, root_dir, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(self.get_directory_tree(root_dir, output_file))
            for dirpath, _, filenames in os.walk(root_dir):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    # 忽略输出文件
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
                # 忽略输出文件
                if os.path.join(dirpath, f) == output_file:
                    continue
                tree.append(f"{subindent}├── {f}")
        return "\n".join(tree) + "\n"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = ProjectExportTool()
    mainWin.show()
    sys.exit(app.exec_())
