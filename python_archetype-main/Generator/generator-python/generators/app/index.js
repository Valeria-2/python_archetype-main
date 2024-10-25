const config = require("./config.json");
var Generator = require('yeoman-generator');

module.exports = class extends Generator {
    initializing() {
        this.props = {
            company: config.company,
            name: config.name,
            port: config.port,
        };
    }

    writing() {
        var done = this.async();

        this.fs.copyTpl(
            this.templatePath('api-service/.env.template'), // Renombrado a .env.template
            this.destinationPath(`${this.props.name.toLowerCase()}-service/.env`), {
                port: this.props.port,
            },
            {
                openDelimiter: '[',
                closeDelimiter: ']'
            }
        );

        this.fs.copyTpl(
            this.templatePath('api-service/**'),
            this.destinationPath(`${this.props.name.toLowerCase()}-service/`), {
            name: this.props.name,
            namelower: this.props.name.toLowerCase(),
            port: this.props.port,
            company: this.props.company,
        },
            {
                openDelimiter: '[',
                closeDelimiter: ']'
            }
        );
        
        this.fs.copyTpl(
            this.templatePath('api-service/*/**/*'),
            this.destinationPath(`${this.props.name.toLowerCase()}-service/`), {
            name: this.props.name,
            namelower: this.props.name.toLowerCase(),
            port: this.props.port,
            company: this.props.company,
        },
            {
                openDelimiter: '[',
                closeDelimiter: ']'
            }
        );

        this.fs.copyTpl(
            this.templatePath('api-service/.gitignore'),
            this.destinationPath(`${this.props.name.toLowerCase()}-service/.gitignore`)
        );

        done();
    }

    install() {
        var done = this.async();
        const facadeTestFileName = `Test${this.props.name}Facade.py`;
        const serviceTestFileName = `Test${this.props.name}Service.py`;

        try {
            process.chdir(`${this.props.name.toLowerCase()}-service`);

            // Ejecutar el script
            this.spawnCommandSync('cmd.exe', ['/c', 'setup.bat']);
            this.spawnCommandSync('del', ['setup.bat']);

            // Ejecutar pruebas unitarias
            process.chdir(`test/facade`);
            this.spawnCommandSync('pytest', [facadeTestFileName]);

            process.chdir('../Services');
            this.spawnCommandSync('pytest', [serviceTestFileName]);

            done();
        } catch (err) {
            done(err);
        }
    }
};
