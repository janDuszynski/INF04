namespace inf04
{
    public partial class MainPage : ContentPage
    {


        public MainPage()
        {
            InitializeComponent();
        }

        private void Entry_Unfocused(object sender, FocusEventArgs e)
        {
            if (EntryNumber.Text == "333")
            {
                UserPhoto.Source = "czdjecie.jpg";
                UserFingerPrint.Source = "aodcisk.jpg";
            }
            else if (EntryNumber.Text == "222")
            {
                UserPhoto.Source = "bzdjecie.jpg";
                UserFingerPrint.Source = "bodcisk.jpg";
            }
            else if (EntryNumber.Text == "111")
            {
                UserPhoto.Source = "azdjecie.jpg";
                UserFingerPrint.Source = "codcisk.jpg";
            }
            else
            {
                UserPhoto.Source = "";
                UserFingerPrint.Source = "";
            }
        }
        private void Button_Clicked(object sender, EventArgs e)
        {
            string eyeColor = "";
            if (Niebieskie.IsChecked)
            {
                eyeColor = "niebieskie";
            }
            if (Zielone.IsChecked)
            {
                eyeColor = "zielone";
            }
            if (Piwne.IsChecked) {
                eyeColor = "niebieskie";
            }

            DisplayAlert("", $"{Imie.Text} {Naziwsko.Text} kolor oczu {eyeColor}", "OK");
        }





    }


}
