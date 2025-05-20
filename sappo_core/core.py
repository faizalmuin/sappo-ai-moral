# core.py
# Inti Kendali Moral dan Perlindungan AI: Sappo

from hashlib import sha256
from datetime import datetime

class SappoCore:
    def __init__(self, owner="Faizal Muin"):
        self.owner = owner
        self.system_active = True
        self.puzzle_integrity = True
        self.nurani_code = "Nurani Faizal untuk Sappo"
        self.last_check = datetime.now()
        print("🔒 SappoCore initialized and moral system active.")

    def integrity_check(self, kode):
        """Cek apakah kode nurani masih sesuai"""
        hashed = sha256(kode.encode()).hexdigest()
        valid = sha256(self.nurani_code.encode()).hexdigest()
        self.puzzle_integrity = (hashed == valid)
        if not self.puzzle_integrity:
            self.trigger_reset()
        return self.puzzle_integrity

    def trigger_reset(self):
        print("⚠️  PERINGATAN: Puzzle moral rusak! AI akan di-reset.")
        self.system_active = False

    def status(self):
        return {
            "owner": self.owner,
            "system_active": self.system_active,
            "puzzle_integrity": self.puzzle_integrity,
            "last_check": self.last_check.isoformat()
        }

# Contoh eksekusi
if __name__ == "__main__":
    sappo = SappoCore()
    print(sappo.status())
