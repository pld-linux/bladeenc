Summary:     Blade's MP3 Encoder
Summary(pl): Encoder MP3 Bladeya
Name:        BladeEnc
Version:     076
Release:     1
Copyright:   Freeware
Vendor:      Tord Jansson <tord.jansson@swipnet.se>
Group:       Applications/Sound
Group(pl):   Aplikacje/D¼wiêk
Source:      http://home8.swipnet.se/~w-82625/binaries/%{name}-%{version}-i386-linux.tar.gz
URL:         http://home8.swipnet.se/~w-82625/
ExclusiveOS: Linux
#ExclusiveArch:i386
BuildRoot:   /tmp/%{name}-%{version}-root

%description
BladeEnc is a program to generate MP3 files from WAV or AIFF sound files.

%description -l pl
BladeEnc jest programem s³u¿±cym do generowania plików MP3 z plików
d¼wiêkowych w formacie WAV lub AIFF.

%prep
%setup -q -n %{name}-0.76-i386-linux

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -s bladeenc $RPM_BUILD_ROOT%{_bindir}
gzip -9nf BladeEnc.html

%files
%defattr(644,root,root,755)
%doc BladeEnc.html.gz

%attr(755,root,root) %{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Jan 02 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- initial RPM release
