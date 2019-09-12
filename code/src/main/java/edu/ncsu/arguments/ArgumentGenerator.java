package edu.ncsu.arguments;

import edu.ncsu.config.Settings;
import edu.ncsu.executors.helpers.FileHandler;
import edu.ncsu.executors.models.*;
import org.apache.commons.lang3.StringUtils;

import java.util.*;
import java.util.concurrent.ThreadLocalRandom;
import java.util.logging.Logger;

public class ArgumentGenerator {

    private static final Logger LOGGER = Logger.getLogger(ArgumentGenerator.class.getName());

    private static final String STRING = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";


    // *********************************************************************************** //
    // PRIMITIVES

    /**
     * @return - A random short value
     */
    private static Short randShort() {
        double probability = Math.random();
        if (probability < 0.1) {
            return randShort(-10, 10);
        } else if (probability < 0.7) {
            return randShort(-100, 100);
        } else if (probability < 0.9) {
            return randShort(-1000, 1000);
        } else {
            return randShort(Short.MIN_VALUE/2, Short.MAX_VALUE/2);
        }
    }

    /**
     * @param low - Low value of range
     * @param high - High value of range
     * @return - Random short value in a range
     */
    private static Short randShort(Integer low, Integer high) {
        return randInteger(low, high).shortValue();
    }


    /**
     * @return - A random integer value
     */
    private static Integer randInteger() {
        double probability = Math.random();
        if (probability < 0.1) {
            return randInteger(-10, 10);
        } else if (probability < 0.7) {
            return randInteger(-100, 100);
        } else if (probability < 0.9) {
            return randInteger(-1000, 1000);
        } else {
            return randInteger((Integer.MIN_VALUE + 2)/2, Integer.MAX_VALUE/2);
        }
    }

    /**
     * @param low - Low value of range
     * @param high - High value of range
     * @return - Random integer value in range.
     */
    private static Integer randInteger(Integer low, Integer high) {
        return ThreadLocalRandom.current().nextInt(low, high + 1);
    }

    /**
     * @return - random long value
     */
    private static Long randLong() {
        double probability = Math.random();
        if (probability < 0.1) {
            return randLong(-10L, 10L);
        } else if (probability < 0.7) {
            return randLong(-100L, 100L);
        } else if (probability < 0.9) {
            return randLong(-1000L, 1000L);
        } else {
            return randLong((Long.MIN_VALUE + 2)/2, Long.MAX_VALUE/2);
        }
    }

    /**
     * @param low - Low value of range
     * @param high - High value of range
     * @return - Return a random long value
     */
    private static Long randLong(Long low, Long high) {
        return ThreadLocalRandom.current().nextLong(low, high + 1);
    }

    /**
     * @return - A random float value
     */
    private static Float randFloat() {
        double probability = Math.random();
        if (probability < 0.1) {
            return randFloat(-10.0f, 10.0f);
        } else if (probability < 0.7) {
            return randFloat(-100.0f, 100.0f);
        } else if (probability < 0.9) {
            return randFloat(-1000.0f, 1000.0f);
        } else {
            return randFloat((Float.MIN_VALUE + 2)/2, Float.MAX_VALUE/2);
        }
    }

    /**
     * Return
     * @param low - low value of range
     * @param high - high value of range
     * @return - Random float in range
     */
    private static Float randFloat(Float low, Float high) {
        return (float) ThreadLocalRandom.current().nextDouble(low, high + 1);
    }

    /**
     * @return - A random double value
     */
    private static Double randDouble() {
        double probability = Math.random();
        if (probability < 0.1) {
            return randDouble(-10.0, 10.0);
        } else if (probability < 0.7) {
            return randDouble(-100.0, 100.0);
        } else if (probability < 0.9) {
            return randDouble(-1000.0, 1000.0);
        } else {
            return randDouble((Double.MIN_VALUE + 2)/2, Double.MAX_VALUE/2);
        }
    }

    /**
     * Return
     * @param low - low value of range
     * @param high - high value of range
     * @return - Random double in range
     */
    private static Double randDouble(Double low, Double high) {
        return ThreadLocalRandom.current().nextDouble(low, high + 1);
    }

    /**
     * @return - A random character
     */
    private static Character randCharacter() {
        return (char) ThreadLocalRandom.current().nextInt(0, 256);
    }

    /**
     * @return - A random boolean
     */
    private static Boolean randBoolean() {
        return ThreadLocalRandom.current().nextBoolean();
    }

    /**
     * @param length - Length of string
     * @return - Random string of a certain length
     */
    private static String randString(int length) {
        StringBuilder sb = new StringBuilder(length);
        for( int i = 0; i < length; i++ )
            sb.append(STRING.charAt(ThreadLocalRandom.current().nextInt(STRING.length())));
        return sb.toString();
    }

    /**
     * @return - Random string
     */
    private static String randString() {
        return randString(ThreadLocalRandom.current().nextInt(1, 20));
    }

    private static Object generateRandomArgument(Primitive argumentType) {
        switch (argumentType) {
            case SHORT:
                return randShort();
            case INTEGER:
                return randInteger();
            case LONG:
                return randLong();
            case FLOAT:
                return randFloat();
            case DOUBLE:
                return randDouble();
            case BOOLEAN:
                return randBoolean();
            case CHARACTER:
                return randCharacter();
            case STRING:
                return randString();
            default:
                throw new RuntimeException(String.format(
                        "Currently we do not support the class %s", argumentType.getName()));
        }
    }

    private static Object generateRandomArgumentForFamily(Primitive argumentType) {
        String family = argumentType.getFamily();
        switch (family) {
            case Primitive.Family.INT_FAMILY:
                return randShort();
            case Primitive.Family.FLOAT_FAMILY:
                return randFloat();
            case Primitive.Family.BOOLEAN_FAMILY:
                return randBoolean();
            case Primitive.Family.CHAR_FAMILY:
                return randCharacter();
            case Primitive.Family.STRING_FAMILY:
                return randString();
            default:
                throw new RuntimeException(String.format(
                        "Currently we do not support the class %s", argumentType.getName()));
        }
    }

    // *********************************************************************************** //
    // Objects and Functions

    public static List<Object> generateArgumentsForFunction(String dataset, Function function, int numArgs) {
        if (!function.isValidArgs()) {
            LOGGER.info(String.format("%s does not contain valid arguments", function.getName()));
            return null;
        }
        String argKey = function.makeArgumentsKey();
        if (StringUtils.isEmpty(argKey)) {
            LOGGER.info(String.format("%s has an empty key", function.getName()));
            return null;
        }
        List<Object> fuzzed = new ArrayList<>();
        for (int i = 0; i< numArgs; i++) {
            List<Object> args = new ArrayList<>();
            for (FunctionVariable variable: function.getArguments()) {
                Map<String, Object> generated = generateArgumentsForFunctionVariable(dataset, variable, variable.getArrayDimensions());
                if (generated != null) {
                    if ((Boolean) generated.get("isArray"))
                        args.add(generated.get("args"));
                    else
                        args.addAll((List) generated.get("args"));

                }
            }
            if (args.size() == 0)
                return null;
            fuzzed.add(args);
        }
        Collections.shuffle(fuzzed);
        return fuzzed;
    }

    public static Map<String, Object> generateArgumentsForFunctionVariable(String dataset, FunctionVariable variable) {
        return generateArgumentsForFunctionVariable(dataset, variable, variable.getArrayDimensions());
    }

    private static Map<String, Object> generateArgumentsForFunctionVariable(String dataset, FunctionVariable variable, int arraySize) {
        Map<String, Object> argsMap = new HashMap<>();
        List<Object> args = new ArrayList<>();
        boolean isArray = false;
        if (arraySize == 0) {
            if (variable.getPrimitive() != null) {
//                 args.add(generateRandomArgument(variable.getPrimitive()));
                // TODO: Uncomment line above and line below to consider for each argument type rather family
                args.add(generateRandomArgumentForFamily(variable.getPrimitive()));
            } else if (variable.isBuiltInType()) {
                String fullName = variable.getFullName();
                if (FileHandler.isInputClass(fullName)) {
                    args.add(FileHandler.getRandomFileContent());
                } else {
                    args.add("");
                }
            } else {
                Constructor constructor = Constructor.getConstructor(dataset, variable.getPackageName(), variable.getDataType());
                if (constructor == null || constructor.getParameters() == null)
                    return null;
                for (FunctionVariable param: constructor.getParameters()) {
                    Map<String, Object> paramArgs = generateArgumentsForFunctionVariable(dataset, param);
                    if (paramArgs != null) {
                        if ((Boolean) paramArgs.get("isArray")) {
                            args.add(paramArgs.get("args"));
                        } else {
                            args.addAll((List) paramArgs.get("args"));
                        }
                    }
                }
                if (args.size() == 0)
                    return null;
            }
        } else {
            isArray = true;
            for (int i = 0; i < randInteger(2, Settings.MAX_ARRAY_SIZE); i++) {
                Map<String, Object> arrArgsForFV = generateArgumentsForFunctionVariable(dataset, variable, arraySize - 1);
                if (arrArgsForFV == null)
                    return null;
                args.add(arrArgsForFV.get("args"));
            }
        }
        argsMap.put("args", args);
        argsMap.put("isArray", isArray);
        return argsMap;
    }

}
