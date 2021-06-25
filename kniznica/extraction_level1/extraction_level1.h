#ifndef EXTRACTION_LEVEL1_H
#define EXTRACTION_LEVEL1_H

#include <Python.h>
#include <QObject>
#include <QDebug>
#include <QSharedDataPointer>
#include <vector>
#include <QWidget>
#include <QMainWindow>
#include <QDir>
#include <string>
#include <iostream>
#include <abstract.h>
#include <memory.h>
#include <numpy/ndarrayobject.h>
#include "extraction_level1_global.h"

class EXTRACTION_LEVEL1_EXPORT Extraction_level1
{
public:
    Extraction_level1();
    void loadScript(const char* scriptPy);
    int classify(const QPixmap& item);

private:
    PyObject *pName=nullptr, *pModule=nullptr, *pFuncLoadModel=nullptr, *pFuncTrainedScript=nullptr;

};

#endif // EXTRACTION_LEVEL1_H
