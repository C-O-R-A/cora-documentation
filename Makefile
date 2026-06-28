# CORA Documentation Makefile
# ─────────────────────────────────────────────────────────────────────────────
# Usage:
#   make html        — build everything (Sphinx + all ROS 2 packages)
#   make ros2docs    — rebuild only ROS 2 package docs
#   make serve       — build and serve locally on http://localhost:8080
#   make clean       — remove _build/
#   make livehtml    — auto-rebuild on changes (requires sphinx-autobuild)
#
# Prerequisites:
#   pip install sphinx myst-parser sphinx-autodoc-typehints sphinx-autobuild
#   pip install rosdoc2
#   source /opt/ros/jazzy/setup.bash
# ─────────────────────────────────────────────────────────────────────────────

SPHINXBUILD = sphinx-build
SOURCEDIR   = .
BUILDDIR    = _build
HTMLDIR     = $(BUILDDIR)/html
ROS2_OUT    = $(HTMLDIR)/api/ros2

# Canonical source roots — build only from src/, never install/ or build/
SRC_COMMON  = ../cora_common/src
SRC_DESKTOP = ../cora_desktop/src
SRC_ROBOT   = ../cora_robot/src

# ─────────────────────────────────────────────────────────────────────────────
.PHONY: help html ros2docs retheme serve livehtml clean \
        _sphinx \
        _ros2_cora_bringup _ros2_cora_codi _ros2_cora_description \
        _ros2_cora_gripper_1_description _ros2_cora_moveit_config \
        _ros2_cora_moveit_cpp _ros2_cora_moveit _ros2_cora_msgs \
        _ros2_cora_vision \
        _ros2_cora_gazebo _ros2_odrive_ros2_control \
        _retheme_ros2

help:
	@echo ""
	@echo "  make html       Build everything (Sphinx + all ROS 2 packages)"
	@echo "  make ros2docs   Rebuild only ROS 2 package docs"
	@echo "  make serve      Build then serve at http://localhost:8080"
	@echo "  make livehtml   Auto-rebuild on changes"
	@echo "  make clean      Remove _build/"
	@echo ""

# ─────────────────────────────────────────────────────────────────────────────
# Full build
# ─────────────────────────────────────────────────────────────────────────────
html: _sphinx ros2docs
	@echo ""
	@echo "✓ Build complete → $(HTMLDIR)/index.html"

# ─────────────────────────────────────────────────────────────────────────────
# Sphinx — hand-authored pages + Python SDK autodoc
# ─────────────────────────────────────────────────────────────────────────────
_sphinx:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(HTMLDIR) --keep-going
	@touch $(HTMLDIR)/.nojekyll
	@python3 -c "from pathlib import Path; pkgs=['cora_bringup','cora_codi','cora_description','cora_gripper_1_description','cora_moveit_config','cora_moveit_cpp','cora_moveit','cora_msgs','cora_vision','cora_gazebo','odrive_ros2_control']; out=Path('$(ROS2_OUT)'); out.mkdir(parents=True, exist_ok=True); [(out/f'{p}.html').write_text(f'<!DOCTYPE html><html><head><meta http-equiv=\"refresh\" content=\"0; url={p}/{p}/index.html\"><script>window.location.replace(\"{p}/{p}/index.html\")</script></head><body><a href=\"{p}/{p}/index.html\">{p}</a></body></html>') for p in pkgs]; print('  \u2713 ros2 redirects written')" 

# ─────────────────────────────────────────────────────────────────────────────
# ROS 2 docs — one target per package
# All source packages live under cora_common/src/ except where noted.
# ─────────────────────────────────────────────────────────────────────────────
ros2docs: \
    _ros2_cora_bringup \
    _ros2_cora_codi \
    _ros2_cora_description \
    _ros2_cora_gripper_1_description \
    _ros2_cora_moveit_config \
    _ros2_cora_moveit_cpp \
    _ros2_cora_moveit \
    _ros2_cora_msgs \
    _ros2_cora_vision \
    _ros2_cora_gazebo \
    _ros2_odrive_ros2_control \
    _retheme_ros2

# Re-apply CORA theme over rosdoc2's forced sphinx_rtd_theme
_retheme_ros2:
	@echo "\u2192 Applying CORA theme to ROS 2 docs\u2026"
	python3 retheme_ros2docs.py $(ROS2_OUT)
	@echo "\u2713 Rethemed"

# Run retheme alone without rebuilding packages
retheme:
	python3 retheme_ros2docs.py $(ROS2_OUT)

# ── cora_common packages ──────────────────────────────────────────────────────
_ros2_cora_bringup:
	@echo "→ cora_bringup"
	@mkdir -p $(ROS2_OUT)/cora_bringup
	rosdoc2 build --package-path $(SRC_COMMON)/cora_bringup \
	    --output-dir $(ROS2_OUT)/cora_bringup \
	    || echo "  ⚠  cora_bringup skipped"

_ros2_cora_codi:
	@echo "→ cora_codi"
	@mkdir -p $(ROS2_OUT)/cora_codi
	rosdoc2 build --package-path $(SRC_COMMON)/cora_codi \
	    --output-dir $(ROS2_OUT)/cora_codi \
	    || echo "  ⚠  cora_codi skipped"

_ros2_cora_description:
	@echo "→ cora_description"
	@mkdir -p $(ROS2_OUT)/cora_description
	rosdoc2 build --package-path $(SRC_COMMON)/cora_description \
	    --output-dir $(ROS2_OUT)/cora_description \
	    || echo "  ⚠  cora_description skipped"

_ros2_cora_gripper_1_description:
	@echo "→ cora_gripper_1_description"
	@mkdir -p $(ROS2_OUT)/cora_gripper_1_description
	rosdoc2 build --package-path $(SRC_COMMON)/cora_gripper_1_description \
	    --output-dir $(ROS2_OUT)/cora_gripper_1_description \
	    || echo "  ⚠  cora_gripper_1_description skipped"

_ros2_cora_moveit_config:
	@echo "→ cora_moveit_config"
	@mkdir -p $(ROS2_OUT)/cora_moveit_config
	rosdoc2 build --package-path $(SRC_COMMON)/cora_moveit_config \
	    --output-dir $(ROS2_OUT)/cora_moveit_config \
	    || echo "  ⚠  cora_moveit_config skipped"

_ros2_cora_moveit_cpp:
	@echo "→ cora_moveit_cpp"
	@mkdir -p $(ROS2_OUT)/cora_moveit_cpp
	rosdoc2 build --package-path $(SRC_COMMON)/cora_moveit_cpp \
	    --output-dir $(ROS2_OUT)/cora_moveit_cpp \
	    || echo "  ⚠  cora_moveit_cpp skipped"

_ros2_cora_moveit:
	@echo "→ cora_moveit"
	@mkdir -p $(ROS2_OUT)/cora_moveit
	rosdoc2 build --package-path $(SRC_COMMON)/cora_moveit \
	    --output-dir $(ROS2_OUT)/cora_moveit \
	    || echo "  ⚠  cora_moveit skipped"

_ros2_cora_msgs:
	@echo "→ cora_msgs"
	@mkdir -p $(ROS2_OUT)/cora_msgs
	rosdoc2 build --package-path $(SRC_COMMON)/cora_msgs \
	    --output-dir $(ROS2_OUT)/cora_msgs \
	    || echo "  ⚠  cora_msgs skipped"

_ros2_cora_vision:
	@echo "→ cora_vision"
	@mkdir -p $(ROS2_OUT)/cora_vision
	rosdoc2 build --package-path $(SRC_COMMON)/cora_vision \
	    --output-dir $(ROS2_OUT)/cora_vision \
	    || echo "  ⚠  cora_vision skipped"


# ── cora_desktop-only packages ────────────────────────────────────────────────
_ros2_cora_gazebo:
	@echo "→ cora_gazebo"
	@mkdir -p $(ROS2_OUT)/cora_gazebo
	rosdoc2 build --package-path $(SRC_DESKTOP)/cora_gazebo \
	    --output-dir $(ROS2_OUT)/cora_gazebo \
	    || echo "  ⚠  cora_gazebo skipped"

# ── cora_robot-only packages ──────────────────────────────────────────────────
_ros2_odrive_ros2_control:
	@echo "→ odrive_ros2_control"
	@mkdir -p $(ROS2_OUT)/odrive_ros2_control
	rosdoc2 build --package-path $(SRC_ROBOT)/odrive_ros2_control \
	    --output-dir $(ROS2_OUT)/odrive_ros2_control \
	    || echo "  ⚠  odrive_ros2_control skipped"

# ─────────────────────────────────────────────────────────────────────────────
serve: html
	@echo "Serving at http://localhost:8080 …"
	cd $(HTMLDIR) && python3 -m http.server 8080

livehtml:
	sphinx-autobuild $(SOURCEDIR) $(HTMLDIR) \
	    --watch ../codi/src \
	    --ignore "*.pyc" \
	    --ignore "_build/*"

clean:
	rm -rf $(BUILDDIR)
	@echo "✓ Cleaned $(BUILDDIR)/"