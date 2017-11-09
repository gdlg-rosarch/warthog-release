Name:           ros-indigo-warthog-control
Version:        0.0.2
Release:        0%{?dist}
Summary:        ROS warthog_control package

Group:          Development/Libraries
License:        BSD
URL:            http://www.clearpathrobotics.com/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-controller-manager
Requires:       ros-indigo-diff-drive-controller
Requires:       ros-indigo-interactive-marker-twist-server
Requires:       ros-indigo-joint-state-controller
Requires:       ros-indigo-joy
Requires:       ros-indigo-robot-localization
Requires:       ros-indigo-rosserial-server
Requires:       ros-indigo-teleop-twist-joy
Requires:       ros-indigo-topic-tools
Requires:       ros-indigo-twist-mux
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslaunch

%description
Controllers for Warthog

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Nov 09 2017 Tony Baltovski <tbaltovski@clearpathrobotics.com> - 0.0.2-0
- Autogenerated by Bloom

* Mon Oct 03 2016 Tony Baltovski <tbaltovski@clearpathrobotics.com> - 0.0.1-0
- Autogenerated by Bloom

