// node.js 调用系统命令

const exec = require('child_process').exec
const execPython = (args) => {
  exec('python ./python/divider.py ' + args , (error, stdout, stderr) => {
    if (stdout.length > 1) {
      console.log('you offer args:', stdout);
    } else {
      console.log('you don\'t offer args');
    }
    if (error) {
      console.info('stderr : ' + stderr);
    }
  })
}

module.exports ={
  execPython: execPython
}
