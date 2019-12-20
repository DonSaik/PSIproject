
message = dict({
    "type": "error-msg",
    "content": "",
})

def len_validator(val, min_len, max_len):
    l = len(val)
    if l == 0:
        message["content"] = 'Input is empty....'
    if l < min_len:
        message["content"] = 'Input is too short, min length ' + str(min_len)
    if l > max_len:
        message["content"] = 'Input is too long, max length ' + str(max_len)

    return message

def password_validator(val, val2, msg="passwords do not match"):
    if val != val2:
        message["content"] = msg
    return message

def unique_validator(callback, msg):
    exists = callback()
    if exists:
        message['content'] = msg

    return message