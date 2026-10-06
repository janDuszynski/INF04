namespace czerwiec22
{
    public partial class MainPage : ContentPage
    {
        private int likes = 0;

        public MainPage()
        {
            InitializeComponent();
        }

        private void Polub_Clicked(object sender, EventArgs e)
        {
            likes++;
            ShowLikes();
        }

        private void Usun_Clicked(object sender, EventArgs e)
        {
            if (likes > 0)
            {
                likes--;
            }
            ShowLikes();
        }

        private void ShowLikes()
        {
            likesLabel.Text = $"{likes} polubień";
        }
    }
}
