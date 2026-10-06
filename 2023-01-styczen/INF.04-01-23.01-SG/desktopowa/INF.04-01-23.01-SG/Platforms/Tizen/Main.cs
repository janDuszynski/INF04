using Microsoft.Maui;
using Microsoft.Maui.Hosting;
using System;

namespace INF._04_01_23._01_SG
{
    internal class Program : MauiApplication
    {
        protected override MauiApp CreateMauiApp() => MauiProgram.CreateMauiApp();

        static void Main(string[] args)
        {
            var app = new Program();
            app.Run(args);
        }
    }
}
