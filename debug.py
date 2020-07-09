def debug(func):
  def wrapped(*args, **kwargs):
    from datetime import datetime
    time_from = datetime.now()
    result = func(*args, **kwargs)
    work_time = datetime.now() - time_from
    print(
      func.__name__,
      f"{work_time.microseconds}ms",
      f"args: [{', '.join(args)}]",
      f"kwargs: [{', '.join(kwargs)}]",
      f"result: `{result}`",
      sep='\t'
    )
    return func(*args, **kwargs)
  return wrapped
