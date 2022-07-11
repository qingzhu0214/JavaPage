dsjpt-common/exception文件

先自定义异常BusinessException，继承自RuntimeException

全局异常处理：@ControllerAdvice和@ExceptionHandler(value = BusinessException.class)注解

单使用@ExceptionHandler，只能在当前Controller中处理异常。但当配合@ControllerAdvice一起使用的时候，则可以全局捕获。

