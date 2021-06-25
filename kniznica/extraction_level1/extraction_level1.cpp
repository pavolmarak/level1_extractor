#include "extraction_level1.h"

Extraction_level1::Extraction_level1()
{
    Py_Initialize();
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("import os");
    PyRun_SimpleString("sys.path.append(os.getcwd())");

}


void Extraction_level1::loadScript(const char* scriptPy){


    pName = PyUnicode_FromString(scriptPy);
    pModule = PyImport_Import(pName);


    if(!pModule){
        PyErr_Print();
        printf("ERROR IN PMODULE");
        exit(1);
    }


    std::cout << pModule << std::endl;
    if (pModule != NULL) {
        pFuncLoadModel = PyObject_GetAttrString(pModule,"loadModel");
        pFuncTrainedScript = PyObject_GetAttrString(pModule,"trainedScript");

        if (pFuncLoadModel && PyCallable_Check(pFuncLoadModel)) {
            PyObject_CallFunction(pFuncLoadModel, NULL);
        }
    }
}


int Extraction_level1::classify(const QPixmap& item){
    PyObject* pValue;
    int64_t result = -1;

    if (pModule != NULL) {
        if (pFuncTrainedScript && PyCallable_Check(pFuncTrainedScript)) {
            import_array1(-1);
            const QImage image = item.toImage();
            const int width = image.width();
            const int height = image.height();
            npy_intp dim[] = {height,width};
            std::vector<uchar> imageData;

            for (int i=0;i<height;i++) {
                for (int j=0;j<width;j++){
                    imageData.push_back(qGray(image.pixel(j,i)));
                }
            }

            PyObject* imageArray;
            imageArray = PyArray_SimpleNewFromData(2, dim, NPY_UINT8,reinterpret_cast<void*>(imageData.data()));
            pValue = PyObject_CallFunction(pFuncTrainedScript, "O", imageArray);

            if (pValue != NULL) {
                result = PyLong_AsLong(pValue);
                std::cout << "Success: " << result << std::endl;
            }
            else {
                PyErr_Print();
                fprintf(stderr,"Call failed\n");
                return result;
            }
        }
        else {
            if (PyErr_Occurred())
                PyErr_Print();
            fprintf(stderr, "Cannot find function \"trainedScript\"\n");
        }
        return result;
    }
    else {
        PyErr_Print();
        fprintf(stderr, "Failed to load \"trainedScript\"\n");
        return -1;
    }
    if (Py_FinalizeEx() < 0) {
        return -2;
    }
}
