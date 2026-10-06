namespace styczen26
{
    public class Kosc
    {
        public static int LiczbaInstancji = 0;
        public string[] NazwyPlikow = { "kosc0.png", "kosc1.png", "kosc2.png", "kosc3.png", "kosc4.png", "kosc5.png", "kosc6.png" };
        public int LiczbaOczek;
        public int IdPliku;
        public bool Dostepna;

        private static Random generator = new Random();

        public Kosc()
        {
            LiczbaOczek = generator.Next(1, 7);
            IdPliku = LiczbaOczek;
            Dostepna = true;
            LiczbaInstancji++;
        }

        public Kosc(int wartosc)
        {
            if (wartosc < 1 || wartosc > 6)
            {
                wartosc = 0;
            }
            LiczbaOczek = wartosc;
            IdPliku = wartosc;
            Dostepna = true;
            LiczbaInstancji++;
        }

        public void Rzut()
        {
            if (Dostepna)
            {
                LiczbaOczek = generator.Next(1, 7);
                IdPliku = LiczbaOczek;
            }
        }

        public void Blokuj()
        {
            Dostepna = false;
        }
    }
}
