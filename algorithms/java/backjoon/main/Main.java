package main;

import java.util.List;

import java.lang.reflect.*;
import main.solution.*;

public class Main {
    public static void main(String[] args) throws Exception {
        if (args.length != 2) {
            System.out.println("Usage: <PROBLEM NUMBER> <TEST TEXT PATH>");
            return;
        }

        Method parse = getMethod("main.solution.Solution", "parse", String.class);
        Method solve = getMethod(String.format("main.solution.Solution%s", args[0]), "solve", List.class);

        Object testText = parse.invoke(null, String.format("main/texts/%s", args[1]));
        solve.invoke(null, testText);
    }

    private static Method getMethod(String className, String methodName, Class<?>... parameterTypes) throws Exception {
        Class<?> solution = Class.forName(className);
        return solution.getDeclaredMethod(methodName, parameterTypes);
    }
}
