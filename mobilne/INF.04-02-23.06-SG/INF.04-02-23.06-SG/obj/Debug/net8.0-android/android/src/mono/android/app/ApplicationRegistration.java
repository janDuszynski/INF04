package mono.android.app;

public class ApplicationRegistration {

	public static void registerApplications ()
	{
				// Application and Instrumentation ACWs must be registered first.
		mono.android.Runtime.register ("INF._04_02_23._06_SG.MainApplication, INF.04-02-23.06-SG, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null", crc64827e4583b5212c60.MainApplication.class, crc64827e4583b5212c60.MainApplication.__md_methods);
		mono.android.Runtime.register ("Microsoft.Maui.MauiApplication, Microsoft.Maui, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null", crc6488302ad6e9e4df1a.MauiApplication.class, crc6488302ad6e9e4df1a.MauiApplication.__md_methods);
		
	}
}
