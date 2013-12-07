%define debug_package %{nil}

%define	minor_version 1054
%define major 0
%define minor 10
%define libname %mklibname juffed %{major}.%{minor}
%define libengine %mklibname juffed-engine %{major}.%{minor}
%define devname %mklibname -d juffed %{major}

Name:		juffed
Version: 	0.10
Release: 	5
License:	GPLv2
Source0:	http://sourceforge.net/projects/juffed/files/Releases/%{version}/%{name}-%{version}-%{minor_version}.tar.bz2
Url:		http://juffed.com
Group:		Editors
Summary:	Simple tabbed text editor
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist
BuildRequires:	qscintilla-qt4-devel
BuildRequires:	pkgconfig(enca)
BuildRequires:	qtsingleapplication-devel
Requires:	%{libname} = %{version}-%{release}

%package -n %{libname}
Summary:    %{summary} libraries
Group:      System/Libraries

%description -n %{libname}
%{summary} libraries

%package -n	%{libengine}
Summary:	%{summary} libraries
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{libengine}
%{summary} libraries

%package -n	%{devname}
Summary:	Development package for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
%{summary}

%package	plugins
Summary:	Plugins for juffed
Group:		Development/Other
Requires:	%{name}-plugin-doclist
Requires:	%{name}-plugin-favorites
Requires:	%{name}-plugin-findinfiles
Requires:	%{name}-plugin-filemanager
Requires:	%{name}-plugin-sort
Requires:	%{name}-plugin-symbolbrowser
Requires:	%{name}-plugin-xmlformat
Requires:	%{name}-plugin-keybindings

%description	plugins
%{summary}
See http://code.google.com/p/juffed-plugins/wiki/JuffEd_Plugins_Tutorial 
for details.

%package	plugin-autosave
Summary:	AutoSave plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description	plugin-autosave
%{summary}

%package	plugin-colorpicker
Summary:	Color picker plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description	plugin-colorpicker
%{summary}

%package	plugin-keybindings
Summary:	Keybindings plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description	plugin-keybindings
%{summary}

%package	plugin-doclist
Summary:	DocList plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-doclist < %{version}-%{release}

%description	plugin-doclist
%{summary}

%package	plugin-favorites
Summary:	Favorites plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-favorites < %{version}-%{release}

%description	plugin-favorites
%{summary}

%package	plugin-findinfiles
Summary:	FindInFiles plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-findinfiles < %{version}-%{release}

%description	plugin-findinfiles
%{summary}

%package	plugin-filemanager
Summary:	FileManager plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-filemanager < %{version}-%{release}

%description	plugin-filemanager
%{summary}

%package	plugin-sort
Summary:	SortDocument plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-sort < %{version}-%{release}

%description	plugin-sort
%{summary}

%package	plugin-symbolbrowser
Summary:	SymbolBrowser plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-symbolbrowser < %{version}-%{release}

%description	plugin-symbolbrowser
%{summary}

%package	plugin-xmlformat
Summary:	XMLFormat plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-xmlformat < %{version}-%{release}

%description	plugin-xmlformat
%{summary}

%package	plugin-todolist
Summary:	TODO list plugin for juffed
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-plugin-todolist < %{version}-%{release}

%description	plugin-todolist
%{summary}

%description
Simple tabbed text editor with syntax highlighting for:
	- C++
	- Python
	- HTML
	- PHP
	- XML
	- TeX
	- Makefiles
	- ini-files
	- patch-files

%prep
%setup -q 
%{__rm} -rf src/3rd_party
%{__rm} -rf plugins/terminal/qtermwidget

%build
#cmake -DCMAKE_BUILD_TYPE=release -DUSE_SYSTEM_QTSINGLEAPPLICATION=ON
mkdir build
pushd build
cmake ../ -DCMAKE_BUILD_TYPE=release \
	-DUSE_SYSTEM_QTSINGLEAPPLICATION=ON \
	-DBUILD_TODOLIST=ON \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir}

%make

%install
%makeinstall_std -C build

%files
%doc COPYING ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files -n %{libname}
%{_libdir}/libjuff.so.*

%files -n %{libengine}
%{_libdir}/libjuffed-engine-qsci.so.%{version}

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/libjuffed-engine-qsci.so
%{_libdir}/libjuff.so

%files plugins

%files plugin-keybindings
%{_libdir}/%{name}/plugins/libkeybindings.so  

%files plugin-doclist
%{_libdir}/%{name}/plugins/libdoclist.so

%files plugin-favorites
%{_libdir}/%{name}/plugins/libfavorites.so

%files plugin-findinfiles
%{_libdir}/%{name}/plugins/libfindinfiles.so

%files plugin-filemanager
%{_libdir}/%{name}/plugins/libfm.so

%files plugin-sort
%{_libdir}/%{name}/plugins/libsortdocument.so

%files plugin-symbolbrowser
%{_libdir}/%{name}/plugins/libsymbolbrowser.so

%files plugin-xmlformat
%{_libdir}/%{name}/plugins/libxmlformat.so

%files plugin-autosave
%{_libdir}/%{name}/plugins/libautosave.so

%files plugin-colorpicker
%{_libdir}/%{name}/plugins/libcolorpicker.so

%files plugin-todolist
%{_libdir}/%{name}/plugins/libtodolist.so
