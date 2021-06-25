QT += gui\
    quick \
    widgets

TEMPLATE = lib
DEFINES += EXTRACTION_LEVEL1_LIBRARY

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    extraction_level1.cpp

HEADERS += \
    extraction_level1_global.h \
    extraction_level1.h

# Default rules for deployment.
unix {
    target.path = /usr/lib
}
!isEmpty(target.path): INSTALLS += target

#Level1 - Python (for python embedding)
unix:!macx: LIBS += -L$$PWD/../../../../../../usr/lib/ -lpython3.9
INCLUDEPATH += $$PWD/../../../../../../usr/include/python3.9
DEPENDPATH += $$PWD/../../../../../../usr/include/python3.9

#Level1 - Numpy (for work with image)
unix:!macx: LIBS += -L$$PWD/../../../../../../usr/lib/python3.9/site-packages/numpy/core/lib/ -lnpymath
INCLUDEPATH += $$PWD/../../../../../../usr/lib/python3.9/site-packages/numpy/core/include
DEPENDPATH += $$PWD/../../../../../../usr/lib/python3.9/site-packages/numpy/core/include
unix:!macx: PRE_TARGETDEPS += $$PWD/../../../../../../usr/lib/python3.9/site-packages/numpy/core/lib/libnpymath.a
