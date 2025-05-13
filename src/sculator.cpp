#include "sculator.hpp"

#include <QString>
#include <QByteArray>

#include <QGridLayout>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>

extern "C" {
    #include <lualib.h>
    #include <lauxlib.h>
}

Sculator::Sculator() {
    luaState = luaL_newstate();
    luaL_openlibs(luaState);

    QGridLayout *layout = new QGridLayout;
    setLayout(layout);

    QLabel* label = new QLabel("Enter your expression:");
    layout->addWidget(label, 0, 0);

    lineEdit = new QLineEdit;
    layout->addWidget(lineEdit, 0, 1);

    QPushButton* button = new QPushButton("Enter");
    connect(button, SIGNAL(clicked()), this, SLOT(calculate()));
    layout->addWidget(button, 0, 2);

    output = new QLabel("output");
    connect(lineEdit, SIGNAL(returnPressed()), this, SLOT(calculate()));
    layout->addWidget(output, 1, 1);
    layout->setAlignment(output, Qt::AlignHCenter);
}

Sculator::~Sculator() {
    lua_close(luaState);
}

void Sculator::calculate() {
    // The Lua expression to evaluate
    if (lineEdit->text() == "") return;

    QString expression = "return ";
    expression.append(lineEdit->text());
    QByteArray ba = expression.toLatin1();
    const char *lua_expr = ba.data();

    // Execute the Lua code in the string
    if (luaL_dostring(luaState, lua_expr) != LUA_OK) {
        output->setText(QString(lua_tostring(luaState, -1)));
    }

    // Get the result from the Lua stack
    if (lua_isnumber(luaState, -1)) {
        double result = lua_tonumber(luaState, -1);
        output->setText(QString::number(result));
    } else {
        output->setText("Error: Not a number result");
    }
}
