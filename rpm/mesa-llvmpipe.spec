# Conditional building of X11 related things
%bcond_with X11
%define mesa_version 9.2.5

Name:       mesa-llvmpipe

Summary:    Mesa graphics libraries built for LLVMpipe
Version:    9.2.5
Release:    0
Group:      System/Libraries
License:    MIT
URL:        http://www.mesa3d.org/
Source0:    %{name}-%{version}.tar.bz2
Source1:    mesa-llvmpipe-rpmlintrc
Patch0:     eglplatform_no_x11.patch

%if %{with X11}
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(dri2proto) >= 1.1
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  makedepend
%endif
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(talloc)
BuildRequires:  pkgconfig(libudev) >= 160
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig autoconf automake
BuildRequires:  expat-devel >= 2.0
BuildRequires:  python
BuildRequires:  libxml2-python
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  llvm-devel
BuildRequires:  gettext

%description
Mesa is an open-source implementation of the OpenGL specification  -
a system for rendering interactive 3D graphics.


%package libglapi
Summary:    Mesa shared gl api library
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libglapi
Mesa shared gl api library.

%package libGLESv1
Summary:    Mesa libGLESv1 runtime libraries
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv1 = %{version}-%{release}

%description libGLESv1
Mesa libGLESv1 runtime library.

%package libGLESv2
Summary:    Mesa libGLESv2 runtime libraries
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv2 = %{version}-%{release}

%description libGLESv2
Mesa libGLESv2 runtime library.

%package libGLESv2-compat
Summary:    Mesa libGLESv2 runtime compatibility library
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   libGLESv2.so.2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv2.so

%description libGLESv2-compat
Mesa libGLESv2 runtime compatibility library.

%package libEGL
Summary:    Mesa libEGL runtime libraries and DRI drivers
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libEGL = %{version}-%{release}

%description libEGL
Mesa libEGL runtime library.

%package libEGL-compat
Summary:    Mesa libEGL runtime compatibility library
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   libEGL.so.1
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libEGL.so

%description libEGL-compat
Mesa libEGL runtime compatibility library.

%package libglapi-devel
Summary:    Mesa libglapi development package
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   mesa-llvmpipe-libglapi = %{version}-%{release}
Provides:   libglapi-devel

%description libglapi-devel
Mesa libglapi development package.

%package libGLESv1-devel
Summary:    Mesa libGLESv1 development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   mesa-llvmpipe-libGLESv1 = %{version}-%{release}
Provides:   libGLESv1-devel

%description libGLESv1-devel
Mesa libGLESv1 development packages

%package libGLESv2-devel
Summary:    Mesa libGLESv2 development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   mesa-llvmpipe-libGLESv2 = %{version}-%{release}
Provides:   libGLESv2-devel
Obsoletes:   mesa-llvmpipe-libGLESv2-compat

%description libGLESv2-devel
Mesa libGLESv2 development packages

%package libEGL-devel
Summary:    Mesa libEGL development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   mesa-llvmpipe-libEGL = %{version}-%{release}
Provides:   libEGL-devel
Obsoletes:   mesa-llvmpipe-libEGL-compat

%description libEGL-devel
Mesa libEGL development packages

%if %{with X11}
%package libGL
Summary:    Mesa libGL runtime libraries and DRI drivers
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGL = %{version}-%{release}

%description libGL
Mesa libGL runtime library.
%endif

%package libGL-devel
Summary:    Mesa libGL development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
%if %{with X11}
Requires:   mesa-llvmpipe-libGL = %{version}-%{release}
Requires:   libX11-devel
%endif
Provides:   libGL-devel

%description libGL-devel
Mesa libGL development packages

%package dri-drivers-devel
Summary:    Mesa-based DRI development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description dri-drivers-devel
Mesa-based DRI driver development files.

%package dri-swrast-driver
Summary:    Mesa-based DRI drivers
Group:      Graphics/Display and Graphics Adaptation
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   mesa-llvmpipe-dri-drivers = %{version}-%{release}

%description dri-swrast-driver
Mesa-based swrast DRI driver.

%package libwayland-egl-devel
Summary:    Mesa libwayland-egl development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   mesa-llvmpipe-libwayland-egl = %{version}-%{release}
Provides:   libwayland-egl-devel

%description libwayland-egl-devel
Mesa libwayland-egl development packages

%package libwayland-egl
Summary:    Mesa libwayland-egl runtime library
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libwayland-egl
Mesa libwayland-egl runtime libraries


%prep
%setup -q -n %{name}-%{version}/mesa

%if ! %{with X11}
# eglplatform_no_x11.patch
%patch0 -p1
%endif

%build
%autogen --disable-static \
    --enable-dri \
    --with-dri-drivers=swrast \
    --enable-osmesa=no \
    --enable-gallium-egl \
    --enable-gallium-llvm \
    --with-gallium-drivers=swrast \
%if %{with X11}
    --with-egl-platforms=x11,fbdev,wayland \
    --with-x \
    --enable-glx-tls \
    --enable-glx=yes \
%else
    --with-egl-platforms=fbdev,wayland \
    --disable-glx \
    --disable-xlib-glx \
%endif
    --enable-egl=yes \
    --enable-gles1=yes \
    --enable-gles2=yes

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

# strip out undesirable headers
rm -f $RPM_BUILD_ROOT/etc/drirc
pushd $RPM_BUILD_ROOT%{_includedir}/GL
rm [a-fh-np-wyz]*.h
rm osmesa.h
popd

%post libglapi -p /sbin/ldconfig

%postun libglapi -p /sbin/ldconfig

%post libGLESv1 -p /sbin/ldconfig

%postun libGLESv1 -p /sbin/ldconfig

%post libGLESv2 -p /sbin/ldconfig

%postun libGLESv2 -p /sbin/ldconfig

%post libGLESv2-compat -p /sbin/ldconfig

%postun libGLESv2-compat -p /sbin/ldconfig

%post libEGL -p /sbin/ldconfig

%postun libEGL -p /sbin/ldconfig

%post libEGL-compat -p /sbin/ldconfig

%postun libEGL-compat -p /sbin/ldconfig

%post dri-swrast-driver -p /sbin/ldconfig

%postun dri-swrast-driver -p /sbin/ldconfig

%post libwayland-egl -p /sbin/ldconfig

%postun libwayland-egl -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/egl/egl_gallium.so

%files libglapi
%defattr(-,root,root,-)
%{_libdir}/libglapi.so.0
%{_libdir}/libglapi.so.0.*

%files libGLESv1
%defattr(-,root,root,-)
%{_libdir}/libGLESv1_CM.so.1
%{_libdir}/libGLESv1_CM.so.1.1.0

%files libGLESv2
%defattr(-,root,root,-)
%{_libdir}/libGLESv2.so.2
%{_libdir}/libGLESv2.so.2.0.0

%files libGLESv2-compat
%defattr(-,root,root,-)
%{_libdir}/libGLESv2.so

%files libEGL
%defattr(-,root,root,-)
%{_libdir}/libEGL.so.1
%{_libdir}/libEGL.so.1.0.0

%files libEGL-compat
%defattr(-,root,root,-)
%{_libdir}/libEGL.so

%files libglapi-devel
%defattr(-,root,root,-)
%{_libdir}/libglapi.so

%files libGLESv1-devel
%defattr(-,root,root,-)
%{_libdir}/libGLESv1_CM.so
%{_includedir}/GLES/egl.h
%{_includedir}/GLES/gl.h
%{_includedir}/GLES/glext.h
%{_includedir}/GLES/glplatform.h
%{_libdir}/pkgconfig/glesv1_cm.pc

%files libGLESv2-devel
%defattr(-,root,root,-)
%{_libdir}/libGLESv2.so
%{_includedir}/GLES2/gl2.h
%{_includedir}/GLES2/gl2ext.h
%{_includedir}/GLES2/gl2platform.h
%{_includedir}/GLES3/gl3.h
%{_includedir}/GLES3/gl3ext.h
%{_includedir}/GLES3/gl3platform.h
%{_libdir}/pkgconfig/glesv2.pc

%files libEGL-devel
%defattr(-,root,root,-)
%{_libdir}/libEGL.so
%dir %{_includedir}/EGL
%{_includedir}/EGL/egl.h
%{_includedir}/EGL/eglext.h
%{_includedir}/EGL/eglplatform.h
%{_includedir}/EGL/eglmesaext.h
%dir %{_includedir}/KHR
%{_includedir}/KHR/khrplatform.h
%{_libdir}/pkgconfig/egl.pc

%if %{with X11}
%files libGL
%defattr(-,root,root,-)
%{_libdir}/libGL.so.*
%endif

%files libGL-devel
%defattr(-,root,root,-)
%{_includedir}/GL/gl.h
%{_includedir}/GL/gl_mangle.h
%{_includedir}/GL/glext.h
%{_includedir}/GL/glx.h
%{_includedir}/GL/glx_mangle.h
%{_includedir}/GL/glxext.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/dri_interface.h
%if %{with X11}
%{_libdir}/libGL.so
%endif
%{_libdir}/pkgconfig/gl.pc

%files dri-drivers-devel
%defattr(-,root,root,-)
%{_libdir}/libdricore%{mesa_version}.so
%{_libdir}/pkgconfig/dri.pc

%files dri-swrast-driver
%defattr(-,root,root,-)
%{_libdir}/libdricore%{mesa_version}.so.*
%{_libdir}/dri/swrast_dri.so

%files libwayland-egl-devel
%defattr(-,root,root,-)
%{_libdir}/libwayland-egl.so
%{_libdir}/pkgconfig/wayland-egl.pc

%files libwayland-egl
%defattr(-,root,root,-)
%{_libdir}/libwayland-egl.so.1
%{_libdir}/libwayland-egl.so.1.*
