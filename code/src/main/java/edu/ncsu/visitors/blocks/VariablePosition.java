package edu.ncsu.visitors.blocks;

import com.github.javaparser.Position;

public class VariablePosition extends Position implements Comparable<VariablePosition>{
    /**
     * @param line Line number
     * @param column Column number
     */
    public VariablePosition(Integer line, Integer column) {
        super(line, column);
    }

    /**
     * @param other Instance of Variable
     * @return True if variable is after the current variable
     */
    public boolean isAfter(VariablePosition other) {
        return this.getLine() > other.getLine() || (this.getLine() == other.getLine() && this.getColumn() > other.getColumn());
    }

    /**
     * @param other Instance of Variable
     * @return True if variable is after the current variable
     */
    public boolean isBefore(VariablePosition other) {
        return this.getLine() < other.getLine() || (this.getLine() == other.getLine() && this.getColumn() < other.getColumn());
    }

    @Override
    public int compareTo(VariablePosition o) {
        if (isAfter(o)) {
            return 1;
        } else if (isBefore(o)) {
            return -1;
        }
        return 0;
    }

    @Override
    public String toString() {
        return String.format("%d : %d", this.getLine(), this.getColumn());
    }

}
