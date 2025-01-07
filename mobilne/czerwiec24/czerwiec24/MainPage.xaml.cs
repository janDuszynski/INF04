using System.Linq;
namespace czerwiec24
{
    public partial class MainPage : ContentPage
    {
        public int total_result = 0;
        public MainPage()
        {
            InitializeComponent();
        }
        private void Button_Clicked(object sender, EventArgs e)
        {
            List<int> number = new List<int>();
            Dictionary<int, int> numberCount = new Dictionary<int, int>();
            Random rnd = new Random();

            for (int i = 0; i < 5; i++)
            {
                number.Add(rnd.Next(1, 7));
            }


            Image1.Source = $"k{number[0]}.png";
            Image2.Source = $"k{number[1]}.png";
            Image3.Source = $"k{number[2]}.png";
            Image4.Source = $"k{number[3]}.png";
            Image5.Source = $"k{number[4]}.png";

            int sum = 0;
            foreach(var i in number)
            {
                int count = number.Count(n => n == i);
                if (count > 1) sum += i;
            }
           
            total_result += sum;
            draw_result.Text = $"Wynik losowania: {sum}";
            game_result.Text = $"Wynik gry: {total_result}";
        }




        private void Button_Clicked_1(object sender, EventArgs e)
        {
            draw_result.Text = "Wynik tego losowania: 0";
            game_result.Text = "Wynik gry: 0";
            total_result = 0;
            Image1.Source = Image2.Source = Image3.Source = Image4.Source = Image5.Source = "znak.png";
        }
    }
    
}
