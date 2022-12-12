#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: rmoulin
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import audio
from gnuradio import blocks
from gnuradio import channels
from gnuradio.filter import firdes
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import vocoder
from gnuradio.qtgui import Range, RangeWidget
from gnuradio import qtgui

class manip4(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "manip4")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_symb2 = samp_symb2 = 8
        self.samp_symb1 = samp_symb1 = 8
        self.samp_rate = samp_rate = 32000
        self.resamp2 = resamp2 = 8
        self.resamp1 = resamp1 = 8
        self.noiseVoltage = noiseVoltage = 0
        self.constellation = constellation = 32

        ##################################################
        # Blocks
        ##################################################
        self._samp_symb2_range = Range(2, 128, 2, 8, 200)
        self._samp_symb2_win = RangeWidget(self._samp_symb2_range, self.set_samp_symb2, 'samp_symb2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._samp_symb2_win)
        self._samp_symb1_range = Range(2, 128, 2, 8, 200)
        self._samp_symb1_win = RangeWidget(self._samp_symb1_range, self.set_samp_symb1, 'samp_symb1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._samp_symb1_win)
        self._resamp2_range = Range(2, 128, 1, 8, 200)
        self._resamp2_win = RangeWidget(self._resamp2_range, self.set_resamp2, 'resamp2', "counter_slider", float)
        self.top_grid_layout.addWidget(self._resamp2_win)
        self._resamp1_range = Range(2, 128, 1, 8, 200)
        self._resamp1_win = RangeWidget(self._resamp1_range, self.set_resamp1, 'resamp1', "counter_slider", float)
        self.top_grid_layout.addWidget(self._resamp1_win)
        self._noiseVoltage_range = Range(0, 5, 0.05, 0, 200)
        self._noiseVoltage_win = RangeWidget(self._noiseVoltage_range, self.set_noiseVoltage, 'noiseVoltage', "counter_slider", float)
        self.top_grid_layout.addWidget(self._noiseVoltage_win)
        self._constellation_range = Range(2, 64, 2, 32, 200)
        self._constellation_win = RangeWidget(self._constellation_range, self.set_constellation, 'constellation', "counter_slider", float)
        self.top_grid_layout.addWidget(self._constellation_win)
        self.vocoder_cvsd_encode_fb_0 = vocoder.cvsd_encode_fb(resamp1,0.5)
        self.vocoder_cvsd_decode_bf_0 = vocoder.cvsd_decode_bf(resamp2,0.5)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=8,
                taps=None,
                fractional_bw=None)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.digital_psk_mod_0 = digital.psk.psk_mod(
            constellation_points=constellation,
            mod_code="gray",
            differential=True,
            samples_per_symbol=samp_symb1,
            excess_bw=0.35,
            verbose=False,
            log=False)
        self.digital_psk_demod_0 = digital.psk.psk_demod(
            constellation_points=constellation,
            differential=True,
            samples_per_symbol=samp_symb2,
            excess_bw=0.35,
            phase_bw=6.28/100.0,
            timing_bw=6.28/100.0,
            mod_code="gray",
            verbose=False,
            log=False)
        self.channels_channel_model_0 = channels.channel_model(
            noise_voltage=noiseVoltage,
            frequency_offset=0.0,
            epsilon=1.0,
            taps=[1.0 + 1.0j],
            noise_seed=0,
            block_tags=False)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/rmoulin/Téléchargements/Céline Dion - Pour que tu maimes encore (Clip officiel).wav', True)
        self.audio_sink_0 = audio.sink(44100, '', True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_wavfile_source_0, 0), (self.vocoder_cvsd_encode_fb_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.digital_psk_demod_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_psk_demod_0, 0), (self.vocoder_cvsd_decode_bf_0, 0))
        self.connect((self.digital_psk_mod_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.vocoder_cvsd_decode_bf_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.vocoder_cvsd_encode_fb_0, 0), (self.digital_psk_mod_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "manip4")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_symb2(self):
        return self.samp_symb2

    def set_samp_symb2(self, samp_symb2):
        self.samp_symb2 = samp_symb2

    def get_samp_symb1(self):
        return self.samp_symb1

    def set_samp_symb1(self, samp_symb1):
        self.samp_symb1 = samp_symb1

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_resamp2(self):
        return self.resamp2

    def set_resamp2(self, resamp2):
        self.resamp2 = resamp2

    def get_resamp1(self):
        return self.resamp1

    def set_resamp1(self, resamp1):
        self.resamp1 = resamp1

    def get_noiseVoltage(self):
        return self.noiseVoltage

    def set_noiseVoltage(self, noiseVoltage):
        self.noiseVoltage = noiseVoltage
        self.channels_channel_model_0.set_noise_voltage(self.noiseVoltage)

    def get_constellation(self):
        return self.constellation

    def set_constellation(self, constellation):
        self.constellation = constellation



def main(top_block_cls=manip4, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
