QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    main.cpp \
    mainwindow.cpp

HEADERS += \
    mainwindow.h

FORMS += \
    mainwindow.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target


unix:!macx: LIBS += -L$$PWD/../../../../../../usr/lib/ -lpython3.9
INCLUDEPATH += $$PWD/../../../../../../usr/include/python3.9
DEPENDPATH += $$PWD/../../../../../../usr/include/python3.9


unix:!macx: LIBS += -L$$PWD/../../../../../../usr/lib/python3.9/site-packages/numpy/core/lib/ -lnpymath

INCLUDEPATH += $$PWD/../../../../../../usr/lib/python3.9/site-packages/numpy/core/include
DEPENDPATH += $$PWD/../../../../../../usr/lib/python3.9/site-packages/numpy/core/include

unix:!macx: PRE_TARGETDEPS += $$PWD/../../../../../../usr/lib/python3.9/site-packages/numpy/core/lib/libnpymath.a



unix:!macx: LIBS += -L$$PWD/../build-extraction_level1-Desktop_Qt_5_15_2_GCC_64bit-Debug/ -lextraction_level1

INCLUDEPATH += $$PWD/../extraction_level1
DEPENDPATH += $$PWD/../extraction_level1
