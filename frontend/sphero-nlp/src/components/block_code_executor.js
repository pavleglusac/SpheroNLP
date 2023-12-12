export function executeCode(code, vue_context) {
    let variables = {};

    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }    
    
    async function Program(block) {
        let commands = block['commands'];
        for (let i = 0; i < commands.length; i++) {
            await executeBlock(commands[i]);
        }
    }

    async function RollStatement(block) {
        let degrees = block['degrees'];
        let speed = block['speed'] * 1.75;
        let seconds = block['seconds'];
        console.log("RollStatement called");
        console.log(degrees, speed, seconds);
        vue_context.$eventBus.emit('roll', {degrees, speed, seconds});
        await sleep(seconds * 1000); 
        
    }

    async function LEDStatement(block) {
        let r = block['red'];
        let g = block['green'];
        let b = block['blue'];
        console.log("LEDStatement called");
        // console.log(red, green, blue);
        vue_context.$eventBus.emit('led', {r, g, b});
    }

    async function SoundStatement(block) {
        let sound = block['sound'];
        console.log("SoundStatement called");
        vue_context.$eventBus.emit('sound', sound);
    }

    async function DeclareStatement(block) {
        let name = block['name'];
        let value = block['value'];
        variables[name] = value;
        console.log("DeclareStatement called");
    }

    async function AssignStatement(block) {
        let name = block['name'];
        let value = block['value'];
        variables[name] = value;
        console.log("AssignStatement called");
    }

    async function ResolveCondition(condition) {
        if (condition.name == 'CompareExpression') {
            let left = condition['left'];
            let right = condition['right'];
            // check if variables
            if (left in variables) {
                left = variables[left];
            }
            if (right in variables) {
                right = variables[right];
            }
            let operator = condition['operator'];
            if (operator == '==') {
                condition = left == right;
            } else if (operator == '!=') {
                condition = left != right;
            } else if (operator == '>') {
                condition = left > right;
            } else if (operator == '>=') {
                condition = left >= right;
            } else if (operator == '<') {
                condition = left < right;
            } else if (operator == '<=') {
                condition = left <= right;
            }
        } else if (condition.name == 'Random') {
            let min = condition['min'];
            let max = condition['max'];
            condition = Math.floor(Math.random() * (max - min + 1)) + min;
        } else if (condition.name == 'Literal') {
            condition = condition['value'];
            if (condition in variables) {
                condition = variables[condition];
            }
        }
        console.log("Condition: " + condition);
        return condition;
    }

    async function IfStatement(block) {
        let condition = block['condition'];
        let commands = block['body'];
        condition = ResolveCondition(condition);
        console.log("IfStatement called");

        if (condition) {
            for (let i = 0; i < commands.length; i++) {
                await executeBlock(commands[i]);
            }
        }
    }

    async function ElseStatement(block) {
        console.log("ElseStatement called");
        let body = block['body'];
        for (let i = 0; i < commands.length; i++) {
            await executeBlock(commands[i]);
        }
    }


    async function LoopUntil(block) {
        let condition = block['condition'];
        let commands = block['body'];
        console.log("LoopUntil called");
        condition = ResolveCondition(condition);

        while (!condition) {
            for (let i = 0; i < commands.length; i++) {
                executeBlock(commands[i]);
            }
            condition = ResolveCondition(condition);
        }
    }

    async function LoopTimes(block) {
        let times = block['times'];
        let commands = block['body'];
        console.log("LoopTimes called");

        for (let i = 0; i < times; i++) {
            for (let j = 0; j < commands.length; j++) {
                await executeBlock(commands[j]);
            }
        }
    }

    async function LoopForever(block) {
        let commands = block['body'];
        console.log("LoopForever called");
        while (true) {
            for (let i = 0; i < commands.length; i++) {
                executeBlock(commands[i]);
            }
        }
    }


    async function executeBlock(inner_code) {
        let funcs = {
            'Program': Program,
            'RollStatement': RollStatement,
            'LEDStatement': LEDStatement,
            'SoundStatement': SoundStatement,
            'DeclareStatement': DeclareStatement,
            'AssignStatement': AssignStatement,
            'IfStatement': IfStatement,
            'ElseStatement': ElseStatement,
            'LoopUntil': LoopUntil,
            'LoopTimes': LoopTimes,
            'LoopForever': LoopForever
        }

        let name = inner_code['type'];
        let properties = Object.keys(inner_code);
        // assume name will match a function, dynamically call it using this 
        console.log(funcs);
        console.log(name);

        let func = funcs[name];
        console.log("Executing " + name);
        console.log(func);


        await func(inner_code);
        
        // func(inner_code);
    }

    code = code[2];
    executeBlock(code);

}

