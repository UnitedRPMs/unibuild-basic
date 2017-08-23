Name:           unibuild-basic
Summary:        unibuild-basic metapackage
License:	LGPLv3
Source0: 	https://www.gnu.org/licenses/lgpl-3.0.txt
Version:        0.1
Release:        1%{dist}
Url:            https://unitedrpms.github.io/
Recommends:	x264
Recommends:	x265
Recommends:	xvidcore
Recommends:	faad2
Recommends:	libdca
Recommends:	live555
#Recommends:	mpeg2dec
Recommends:	twolame
Recommends:	vcdimager
Recommends:	aften
Recommends:	opencore-amr
Recommends:	faac
Recommends:	libmms
Recommends:	rtmpdump
Recommends:	libmpeg2
Recommends:	libquicktime
Recommends:	nvenc
Recommends:	mjpegtools
Recommends:	libmng
Recommends:	libdvdcss
Recommends:	vo-aacenc
Recommends:	vo-amrwbenc	  

%description
This is a metapaquete, for the basic construction in URPMS. 
Specifically for a massive rebuild of packages by a release change/new. 


%prep

# Nothing here

%build

# Nothing here

%install

# Nothing here

%files
# Nothing here

%changelog

* Tue Apr 04 2017 David Vásquez <davidjeremias82 AT gmail DOT com> - 0.1-1
- Initial build
