class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, jml_bayar = 1000000):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.jml_bayar = jml_bayar

    def get_jenis(self):
        return self.jenis
    
    def get_jml_bayar(self):
        return self.jml_bayar

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Hunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang dan harus membayar " + "Rp. {:,}".format(self.jml_bayar) + " per bulan."