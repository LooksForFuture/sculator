#ifndef SCULATOR_H
#define SCULATOR_H

#include <QWidget>
#include <QLineEdit>
#include <QLabel>

extern "C" {
    #include <lua.h>
}

class Sculator : public QWidget
{
Q_OBJECT
public:
    explicit Sculator();
    virtual ~Sculator();

private:
    lua_State *luaState;
    QLineEdit *lineEdit;
    QLabel *output;

public slots:
    void calculate();
};

#endif //SCULATOR_H
