package edu.ncsu.executors.models;

import com.google.common.base.MoreObjects;
import org.apache.commons.lang3.StringUtils;

import java.util.List;

public class InputOutput {

    private static final String SEPARATOR = "$|$";

    private List<Object> arguments;

    private Object output;

    private String exceptionMessage;

    public List<Object> getArguments() {
        return arguments;
    }

    public Object getOutput() {
        return output;
    }

    public void setOutput(Object output) {
        this.output = output;
    }

    public String getExceptionMessage() {
        return exceptionMessage;
    }

    public void setExceptionMessage(String exceptionMessage) {
        this.exceptionMessage = exceptionMessage;
    }

    public InputOutput(List<Object> arguments) {
        this.arguments = arguments;
    }

    public InputOutput(List<Object> arguments, Object output, String exceptionMessage) {
        this.arguments = arguments;
        this.output = output;
        this.exceptionMessage = exceptionMessage;
    }

    private String toString(Object object) {
        // TODO: Convert to String
        return null;
    }

    @Override
    public int hashCode() {
        StringBuilder builder = new StringBuilder();
        for (Object argument: arguments) {
            String argString = toString(argument);
            if (builder.length() == 0)
                builder.append(argString);

            else builder.append(SEPARATOR).append(argString);
        }
        return builder.toString().hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof InputOutput))
            return false;
        InputOutput other = (InputOutput) obj;
        if (other.arguments.size() != this.arguments.size())
            return false;
        for (int i=0; i<other.arguments.size(); i++) {
            Object arg1 = this.arguments.get(i);
            Object arg2 = other.arguments.get(i);
            if (!arg1.equals(arg2))
                return false;
        }
        return true;
    }

    protected MoreObjects.ToStringHelper toStringHelper() {
        return MoreObjects.toStringHelper(this).omitNullValues()
                .add("arguments", StringUtils.join(arguments, ","))
                .add("output", output)
                .add("exception", exceptionMessage);
    }

    @Override
    public String toString() {
        return toStringHelper().toString();
    }

}
