import sys
import os
import ctypes
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QGroupBox, 
                             QFormLayout, QSlider, QTextEdit, QFileDialog, 
                             QRadioButton, QMainWindow, QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon

# UKRYWANIE KONSOLI (Dla Windows EXE)
def hide_console():
    if os.name == 'nt':
        console_window = ctypes.windll.kernel32.GetConsoleWindow()
        if console_window != 0:
            ctypes.windll.user32.ShowWindow(console_window, 0)

hide_console()

class LiquidLab(QMainWindow):
    def __init__(self):
        super().__init__()
        self.version = "1.0"
        self.author = "Piotr Gałęziok"
        self.website = "https://github.com/gynsior/liquid-calculator"
        self.email = "mailto:gynsior@gmail.com"
        
        # Gęstości
        self.D_VG = 1.26
        self.D_PG = 1.04
        
        # Języki
        self.current_lang = "PL"
        self.translations = {
            "EN": {
                "title": "Liquid Lab", "recipe_info": "Recipe Info", "name": "Name/No:", 
                "brand": "Aroma Brand:", "target_params": "Target Parameters", "vol": "Volume (ml):",
                "strength": "Target Strength (mg/ml):", "ratio": "VG/PG Ratio:", "stock": "Your Ingredients",
                "shot_str": "Shot Strength (mg):", "shot_ratio": "Shot Ratio (VG%):", "aroma_pct": "Aroma (%):",
                "aroma_base": "Aroma Base:", "calc": "CALCULATE RECIPE", "save": "SAVE TO FILE",
                "legend_vg": "Big clouds, smooth throat hit. For large coils.",
                "legend_pg": "Thin liquid, strong throat hit, best flavor. For Pods.",
                "legend_bal": "Balanced. Standard for most devices.", "error": "COMPOSITION ERROR!",
                "error_desc": "Not physically possible. Decrease VG or use stronger shot.",
                "save_title": "Save Recipe", "summary": "SUMMARY", "recipe": "RECIPE", "ingredients": "INGREDIENTS",
                "grams": "GRAMS", "total": "TOTAL", "ignored": "Ignored in ratio"
            },
            "PL": {
                "title": "Liquid Lab", "recipe_info": "Informacje o przepisie", "name": "Nazwa/Nr:", 
                "brand": "Producent aromatu:", "target_params": "Parametry docelowe", "vol": "Objętość (ml):",
                "strength": "Moc docelowa (mg/ml):", "ratio": "Proporcje VG/PG:", "stock": "Twoje Składniki",
                "shot_str": "Moc shota (mg):", "shot_ratio": "Ratio shota (VG%):", "aroma_pct": "Aromat (%):",
                "aroma_base": "Baza aromatu:", "calc": "OBLICZ RECEPTURĘ", "save": "ZAPISZ RECEPTURĘ",
                "legend_vg": "Duża chmura, łagodny. Wymaga dużych grzałek.",
                "legend_pg": "Rzadki, mocny 'kop', świetny smak. Do Podów.",
                "legend_bal": "Zbalansowany. Standard do większości urządzeń.", "error": "BŁĄD SKŁADU!",
                "error_desc": "Niemożliwe do uzyskania. Zmniejsz VG lub użyj mocniejszego shota.",
                "save_title": "Zapisz recepturę", "summary": "PARAMETRY", "recipe": "RECEPTURA", "ingredients": "SKŁADNIKI",
                "grams": "GRAMY", "total": "SUMA", "ignored": "Zignorowano w ratio"
            },
            "DE": {
                "title": "Liquid Lab", "recipe_info": "Rezept-Info", "name": "Name/Nr:", 
                "brand": "Aroma Marke:", "target_params": "Ziel-Parameter", "vol": "Volumen (ml):",
                "strength": "Zielstärke (mg/ml):", "ratio": "VG/PG Verhältnis:", "stock": "Ihre Zutaten",
                "shot_str": "Shot-Stärke (mg):", "shot_ratio": "Shot-Verhältnis (VG%):", "aroma_pct": "Aroma (%):",
                "aroma_base": "Aroma-Basis:", "calc": "REZEPT BERECHNEN", "save": "SPEICHERN",
                "legend_vg": "Große Wolken, sanfter Zug. Für große Coils.",
                "legend_pg": "Dünne Flüssigkeit, starker Throat-Hit. Für Pods.",
                "legend_bal": "Ausgewogen. Standard für die meisten Geräte.", "error": "ZUSAMMENSETZUNGSFEHLER!",
                "error_desc": "Nicht möglich. Weniger VG oder stärkeren Shot verwenden.",
                "save_title": "Rezept speichern", "summary": "ZUSAMMENFASSUNG", "recipe": "REZEPT", "ingredients": "ZUTATEN",
                "grams": "GRAMM", "total": "GESAMT", "ignored": "Im Verhältnis ignoriert"
            },
            "FR": {
                "title": "Liquid Lab", "recipe_info": "Infos Recette", "name": "Nom/No:", 
                "brand": "Marque d'Arôme:", "target_params": "Paramètres Cibles", "vol": "Volume (ml):",
                "strength": "Taux de Nicotine (mg/ml):", "ratio": "Ratio VG/PG:", "stock": "Vos Ingrédients",
                "shot_str": "Taux du Booster (mg):", "shot_ratio": "Ratio du Booster (VG%):", "aroma_pct": "Arôme (%):",
                "aroma_base": "Base d'Arôme:", "calc": "CALCULER LA RECETTE", "save": "ENREGISTRER",
                "legend_vg": "Gros nuages, hit doux. Pour grosses résistances.",
                "legend_pg": "Liquide fluide, hit fort. Pour les Pods.",
                "legend_bal": "Équilibré. Standard pour la plupart des appareils.", "error": "ERREUR DE COMPOSITION!",
                "error_desc": "Pas possible. Réduisez la VG ou utilisez un booster plus fort.",
                "save_title": "Enregistrer la recette", "summary": "RÉSUMÉ", "recipe": "RECETTE", "ingredients": "INGRÉDIENTS",
                "grams": "GRAMMES", "total": "TOTAL", "ignored": "Ignoré dans le ratio"
            },
            "ES": {
                "title": "Liquid Lab", "recipe_info": "Info Receta", "name": "Nombre/No:", 
                "brand": "Marca Aroma:", "target_params": "Parámetros Objetivo", "vol": "Volumen (ml):",
                "strength": "Fuerza Objetivo (mg/ml):", "ratio": "Relación VG/PG:", "stock": "Tus Ingredientes",
                "shot_str": "Fuerza del Nicokit (mg):", "shot_ratio": "Ratio Nicokit (VG%):", "aroma_pct": "Aroma (%):",
                "aroma_base": "Base del Aroma:", "calc": "CALCULAR RECETA", "save": "GUARDAR",
                "legend_vg": "Grandes nubes, golpe suave. Para resistencias grandes.",
                "legend_pg": "Líquido fluido, golpe fuerte. Para Pods.",
                "legend_bal": "Equilibrado. Estándar para la mayoría de dispositivos.", "error": "¡ERROR DE COMPOSICIÓN!",
                "error_desc": "No es posible. Reduzca el VG o use un nicokit más fuerte.",
                "save_title": "Guardar Receta", "summary": "RESUMEN", "recipe": "RECETA", "ingredients": "INGREDIENTES",
                "grams": "GRAMOS", "total": "TOTAL", "ignored": "Ignorado en ratio"
            },
            "IT": {
                "title": "Liquid Lab", "recipe_info": "Info Ricetta", "name": "Nome/No:", 
                "brand": "Marca Aroma:", "target_params": "Parametri Obiettivo", "vol": "Volume (ml):",
                "strength": "Forza Obiettivo (mg/ml):", "ratio": "Rapporto VG/PG:", "stock": "I tuoi Ingredienti",
                "shot_str": "Forza del Nicokit (mg):", "shot_ratio": "Ratio Nicokit (VG%):", "aroma_pct": "Aroma (%):",
                "aroma_base": "Base Aroma:", "calc": "CALCOLA RICETTA", "save": "SALVA",
                "legend_vg": "Grandi nuvole, colpo morbido. Per coil grandi.",
                "legend_pg": "Liquido fluido, colpo forte. Per i Pod.",
                "legend_bal": "Bilanciato. Standard per la maggior parte dei dispositivi.", "error": "ERRORE DI COMPOSIZIONE!",
                "error_desc": "Non possibile. Ridurre il VG o usare un nicokit più forte.",
                "save_title": "Salva Ricetta", "summary": "RIEPILOGO", "recipe": "RICETTA", "ingredients": "INGREDIENTI",
                "grams": "GRAMMI", "total": "TOTALE", "ignored": "Ignorato nel rapporto"
            }
        }

        self.initUI()

    def initUI(self):
        self.setWindowTitle(f"{self.translations[self.current_lang]['title']} v{self.version}")
        self.setMinimumWidth(650)
        
        # ŁADOWANIE IKONY
        icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'icon.ico')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        # PASEK MENU
        menubar = self.menuBar()
        lang_menu = menubar.addMenu('Language / Język')
        for lang in ["EN", "PL", "DE", "FR", "ES", "IT"]:
            action = QAction(lang, self)
            action.triggered.connect(lambda checked, l=lang: self.change_lang(l))
            lang_menu.addAction(action)
            
        info_menu = menubar.addMenu('?')
        about_action = QAction('About', self)
        about_action.triggered.connect(self.show_about)
        info_menu.addAction(about_action)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        left_panel = QVBoxLayout()
        right_panel = QVBoxLayout()

        # --- SEKCJA 1: INFO ---
        self.info_group = QGroupBox(self.translations[self.current_lang]['recipe_info'])
        info_layout = QFormLayout()
        self.liquid_name = QLineEdit("Liquid #1")
        self.aroma_brand = QLineEdit("TPA")
        self.lbl_name = QLabel(self.translations[self.current_lang]['name'])
        self.lbl_brand = QLabel(self.translations[self.current_lang]['brand'])
        info_layout.addRow(self.lbl_name, self.liquid_name)
        info_layout.addRow(self.lbl_brand, self.aroma_brand)
        self.info_group.setLayout(info_layout)
        left_panel.addWidget(self.info_group)

        # --- SEKCJA 2: CEL ---
        self.target_group = QGroupBox(self.translations[self.current_lang]['target_params'])
        target_layout = QFormLayout()
        self.v_total = QLineEdit("100")
        self.mg_target = QLineEdit("6")
        self.ratio_slider = QSlider(Qt.Orientation.Horizontal)
        self.ratio_slider.setRange(0, 100); self.ratio_slider.setValue(70)
        
        self.lbl_vol = QLabel(self.translations[self.current_lang]['vol'])
        self.lbl_strength = QLabel(self.translations[self.current_lang]['strength'])
        self.lbl_ratio_title = QLabel(self.translations[self.current_lang]['ratio'])
        self.ratio_label = QLabel("70% VG / 30% PG")
        self.legend_label = QLabel(self.translations[self.current_lang]['legend_vg'])
        self.legend_label.setStyleSheet("color: #666; font-size: 10px;")
        
        self.ratio_slider.valueChanged.connect(self.update_labels)
        
        target_layout.addRow(self.lbl_vol, self.v_total)
        target_layout.addRow(self.lbl_strength, self.mg_target)
        target_layout.addRow(self.lbl_ratio_title, self.ratio_slider)
        target_layout.addRow("", self.ratio_label)
        target_layout.addRow("", self.legend_label)
        self.target_group.setLayout(target_layout)
        left_panel.addWidget(self.target_group)

        # --- SEKCJA 3: STOCK ---
        self.stock_group = QGroupBox(self.translations[self.current_lang]['stock'])
        stock_layout = QFormLayout()
        self.mg_base = QLineEdit("18")
        self.aroma_pct = QLineEdit("10")
        self.nic_ratio_slider = QSlider(Qt.Orientation.Horizontal)
        self.nic_ratio_slider.setRange(0, 100); self.nic_ratio_slider.setValue(50)
        
        self.lbl_shot_str = QLabel(self.translations[self.current_lang]['shot_str'])
        self.lbl_shot_ratio = QLabel(self.translations[self.current_lang]['shot_ratio'])
        self.lbl_aroma_pct = QLabel(self.translations[self.current_lang]['aroma_pct'])
        self.lbl_aroma_base = QLabel(self.translations[self.current_lang]['aroma_base'])
        self.nic_ratio_label = QLabel("50/50")
        
        self.nic_ratio_slider.valueChanged.connect(self.update_labels)

        self.rb_pg = QRadioButton("PG"); self.rb_vg = QRadioButton("VG"); self.rb_none = QRadioButton("N/A")
        self.rb_pg.setChecked(True)
        ar_layout = QHBoxLayout(); ar_layout.addWidget(self.rb_pg); ar_layout.addWidget(self.rb_vg); ar_layout.addWidget(self.rb_none)
        
        stock_layout.addRow(self.lbl_shot_str, self.mg_base)
        stock_layout.addRow(self.lbl_shot_ratio, self.nic_ratio_slider)
        stock_layout.addRow("", self.nic_ratio_label)
        stock_layout.addRow(self.lbl_aroma_pct, self.aroma_pct)
        stock_layout.addRow(self.lbl_aroma_base, ar_layout)
        self.stock_group.setLayout(stock_layout)
        left_panel.addWidget(self.stock_group)

        # --- SEKCJA 4: WYNIKI ---
        self.results_display = QTextEdit(); self.results_display.setReadOnly(True)
        right_panel.addWidget(self.results_display)
        self.calc_btn = QPushButton(self.translations[self.current_lang]['calc'])
        self.calc_btn.clicked.connect(self.calculate)
        self.calc_btn.setStyleSheet("height: 40px; background-color: #2E7D32; color: white; font-weight: bold;")
        self.save_btn = QPushButton(self.translations[self.current_lang]['save'])
        self.save_btn.clicked.connect(self.save_to_file); self.save_btn.setEnabled(False)
        right_panel.addWidget(self.calc_btn); right_panel.addWidget(self.save_btn)

        main_layout.addLayout(left_panel, 1); main_layout.addLayout(right_panel, 1)

    def change_lang(self, lang):
        self.current_lang = lang
        t = self.translations[lang]
        
        # Tytuły
        self.setWindowTitle(f"{t.get('title', 'Liquid Lab')} v{self.version}")
        self.info_group.setTitle(t.get('recipe_info', ''))
        self.target_group.setTitle(t.get('target_params', ''))
        self.stock_group.setTitle(t.get('stock', ''))
        
        # Etykiety
        self.lbl_name.setText(t.get('name', ''))
        self.lbl_brand.setText(t.get('brand', ''))
        self.lbl_vol.setText(t.get('vol', ''))
        self.lbl_strength.setText(t.get('strength', ''))
        self.lbl_ratio_title.setText(t.get('ratio', ''))
        self.lbl_shot_str.setText(t.get('shot_str', ''))
        self.lbl_shot_ratio.setText(t.get('shot_ratio', ''))
        self.lbl_aroma_pct.setText(t.get('aroma_pct', ''))
        self.lbl_aroma_base.setText(t.get('aroma_base', ''))
        
        # Przyciski
        self.calc_btn.setText(t.get('calc', ''))
        self.save_btn.setText(t.get('save', ''))
        
        self.update_labels()

    def update_labels(self):
        vg = self.ratio_slider.value(); pg = 100 - vg
        self.ratio_label.setText(f"<b>{vg}% VG / {pg}% PG</b>")
        t = self.translations[self.current_lang]
        if vg >= 70: self.legend_label.setText(t.get('legend_vg', ''))
        elif vg <= 40: self.legend_label.setText(t.get('legend_pg', ''))
        else: self.legend_label.setText(t.get('legend_bal', ''))
        
        n_vg = self.nic_ratio_slider.value()
        self.nic_ratio_label.setText(f"{n_vg}/{100-n_vg}")

    def show_about(self):
        github_url = "https://github.com/gynsior/liquid-calculator"
        mail_url = "mailto:gynsior@gmail.com"
        
        # Pobieranie ścieżki (bezpieczne dla EXE)
        if getattr(sys, 'frozen', False):
            base_path = os.path.dirname(sys.executable)
            if not os.path.exists(os.path.join(base_path, 'assets', 'icon.ico')):
                base_path = os.path.dirname(__file__)
        else:
            base_path = os.path.dirname(__file__)
        
        icon_path = os.path.join(base_path, 'assets', 'icon.ico')

        msg = QMessageBox(self)
        msg.setWindowTitle("About")

        # Ustawienie natywnej ikony 48x48
        from PyQt6.QtGui import QIcon
        if os.path.exists(icon_path):
            pixmap = QIcon(icon_path).pixmap(128, 128)
            msg.setIconPixmap(pixmap)

        # Treść HTML z precyzyjnym marginesem od ikony
        msg_text = (
            f"<div style='margin-left: 5px;'>"
            f"<h2 style='margin: 0;'>{self.translations[self.current_lang]['title']} v{self.version}</h2>"
            f"<p style='color: #555; margin: 3px 0 10px 0;'>{self.author}</p>"
            f"<hr style='border: 0; border-top: 1px solid #ccc;'>"
            f"<b>Web:</b> <a href='{github_url}'>GitHub</a><br>"
            f"<b>Email:</b> <a href='{mail_url}'>gynsior@gmail.com</a><br><br>"
            f"<i style='font-size: 11px;'>Created for DIY Vapers & Mixing Enthusiasts.</i>"
            f"</div>"
        )

        msg.setText(msg_text)
        msg.setTextFormat(Qt.TextFormat.RichText)
        msg.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        
        # Klucz do sukcesu: Style Sheet, który wyrównuje marginesy okna
        # margin-right balansuje miejsce zajęte przez ikonę po lewej
        msg.setStyleSheet("""
            QLabel#qt_msgbox_label { 
                padding-left: 10px;
                padding-right: 20px;
                min-width: 300px;
            }
            QPushButton {
                min-width: 80px;
                padding: 5px;
            }
        """)
        
        msg.exec()

    def calculate(self):
        try:
            v_tot = float(self.v_total.text()); mg_t = float(self.mg_target.text())
            mg_b = float(self.mg_base.text()); a_pct = float(self.aroma_pct.text())
            t_vg_p = self.ratio_slider.value() / 100; n_vg_p = self.nic_ratio_slider.value() / 100
            t = self.translations[self.current_lang]

            v_aroma = v_tot * (a_pct / 100); v_nic = (v_tot * mg_t) / mg_b
            
            if self.rb_none.isChecked():
                v_rem = v_tot - v_aroma
                add_vg = (v_rem * t_vg_p) - (v_nic * n_vg_p)
                add_pg = (v_rem * (1 - t_vg_p)) - (v_nic * (1 - n_vg_p))
            else:
                ar_vg = v_aroma if self.rb_vg.isChecked() else 0
                ar_pg = v_aroma if self.rb_pg.isChecked() else 0
                add_vg = (v_tot * t_vg_p) - (v_nic * n_vg_p) - ar_vg
                add_pg = (v_tot * (1 - t_vg_p)) - (v_nic * (1 - n_vg_p)) - ar_pg

            if add_vg < -0.01 or add_pg < -0.01:
                self.results_display.setText(f"!!! {t['error']} !!!\n\n{t['error_desc']}")
                self.save_btn.setEnabled(False); return

            w_aroma = v_aroma * (self.D_VG if self.rb_vg.isChecked() else self.D_PG)
            w_nic = v_nic * (n_vg_p * self.D_VG + (1 - n_vg_p) * self.D_PG)
            w_vg = max(0, add_vg) * self.D_VG; w_pg = max(0, add_pg) * self.D_PG
            
            res = f"{t['summary']}: {self.liquid_name.text()} | {v_tot}ml | {mg_t}mg\n"
            res += f"{'='*35}\n{t['recipe']} (ml | {t['grams']}):\n"
            res += f"Aroma:      {v_aroma:>6.2f} ml | {w_aroma:>6.2f}g\n"
            res += f"Nic Shot:   {v_nic:>6.2f} ml | {w_nic:>6.2f}g\n"
            res += f"Pure VG:    {max(0,add_vg):>6.2f} ml | {w_vg:>6.2f}g\n"
            res += f"Pure PG:    {max(0,add_pg):>6.2f} ml | {w_pg:>6.2f}g\n"
            res += f"{'-'*35}\n{t['total']}:      {v_tot:>6.2f} ml | {w_aroma+w_nic+w_vg+w_pg:>6.2f}g\n"
            self.results_display.setText(res); self.save_btn.setEnabled(True)
        except: self.results_display.setText("Error / Błąd")

    def save_to_file(self):
        path, _ = QFileDialog.getSaveFileName(self, self.translations[self.current_lang]['save_title'], f"Recipe_{self.liquid_name.text()}.txt", "Text Files (*.txt)")
        if path:
            with open(path, "w", encoding="utf-8") as f: f.write(self.results_display.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv); ex = LiquidLab(); ex.show(); sys.exit(app.exec())